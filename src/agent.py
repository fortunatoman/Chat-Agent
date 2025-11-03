import logging
from typing import Callable

import query_tools
from openai import OpenAI

SUMMARIZATION_FUNC_MAP = {
    "summarize_metagpt": query_tools.summarize_metagpt,
    "summarize_autogen": query_tools.summarize_autogen,
}

RAG_FUNC_MAP = {
    "rag_metagpt": query_tools.rag_metagpt,
    "rag_autogen": query_tools.rag_autogen,
    "rag_metagpt_and_autogen": query_tools.rag_metagpt_and_autogen,
}

SYS_MESSAGE = "You are an intelligent AI assistant tasked with tool selection. You MUST return a tool/function given a query."


client = OpenAI()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


def tool_builder(func_map: dict[str, Callable]) -> list[dict]:
    """
    Build tools object required completions API call
    https://platform.openai.com/docs/api-reference/chat/create#chat-create-tools
    """
    tools = []
    for func in func_map.values():
        tools.append(
            {
                "type": "function",
                "function": {
                    "description": func.__doc__,
                    "name": func.__name__,
                },
            }
        )
    return tools


def select_tool(query: str, func_map: dict[str, Callable]) -> str:
    """
    Given a set of tools, select the best tool for the query

    Returns: tool name used for key lookup in func_map
    """
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": SYS_MESSAGE},
            {"role": "user", "content": query},
        ],
        tools=tool_builder(func_map),
    )

    # This needs to be validated
    function_name = response.choices[0].message.tool_calls[0].function.name
    logging.info(f"Selected tool: {function_name}")
    return function_name


def get_summarization_map() -> dict[str, Callable]:
    """Used if query mentions summarization"""
    return SUMMARIZATION_FUNC_MAP


def get_rag_map() -> dict[str, Callable]:
    """Used if query DOES NOT mention summarization"""
    return RAG_FUNC_MAP


HIGH_LEVEL_FUNC_MAP = {
    "get_summarization_map": get_summarization_map,
    "get_rag_map": get_rag_map,
}


def runner(query: str) -> dict:
    """Executes a query using a hierarchical tool selection process"""
    tools_used = []

    # select high level tool (e.g. select RAG or summarization)
    tool_name = select_tool(query=query, func_map=HIGH_LEVEL_FUNC_MAP)
    low_level_func_map = HIGH_LEVEL_FUNC_MAP[tool_name]()
    tools_used.append(tool_name)

    # select low level tool (e.g. select rag_metagpt, rag_autogen, etc.)
    tool_name = select_tool(query, low_level_func_map)
    query_func = low_level_func_map[tool_name]
    response = query_func(query)
    tools_used.append(tool_name)

    response_obj = {
        "tools_used": tools_used,
        "response": response,
    }
    logging.info(response_obj)
    return response_obj
