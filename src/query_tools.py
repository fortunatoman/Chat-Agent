from query import rag_query, summarization_query


def summarize_metagpt(query: str) -> str:
    """Used to summarize the MetaGPT paper."""
    return summarization_query("data/metagpt/MetaGPT.pdf", query)


def summarize_autogen(query: str) -> str:
    """Used to summarize the AutoGen paper."""
    return summarization_query("data/autogen/AutoGen.pdf", query)


def rag_metagpt(query: str) -> str:
    """Used for queries on the MetaGPT paper."""
    return rag_query("data/metagpt", query)


def rag_autogen(query: str) -> str:
    """Used for queries on the AutoGen paper."""
    return rag_query("data/autogen", query)


def rag_metagpt_and_autogen(query: str) -> str:
    """Used if BOTH the MetaGPT and AutoGen papers are mentioned."""
    return rag_query("data", query)
