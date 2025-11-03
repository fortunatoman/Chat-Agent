import agent


class TestSelectLowLevelTool:

    def test_select_rag_autogen(self):
        response = agent.select_tool(
            "What is conversation programming and how does autogen use it?",
            agent.RAG_FUNC_MAP,
        )
        assert response == "rag_autogen"

    def test_select_rag_metagpt(self):
        response = agent.select_tool(
            "What communication protocols are best for metagpt?",
            agent.RAG_FUNC_MAP,
        )
        assert response == "rag_metagpt"

    def test_select_rag_metagpt_and_autogen(self):
        response = agent.select_tool(
            "Compare and contrast how metagpt and autogen handle roles.",
            agent.RAG_FUNC_MAP,
        )
        assert response == "rag_metagpt_and_autogen"

    def test_select_summarize_metagpt(self):
        response = agent.select_tool(
            "Summarize the metagpt paper.",
            agent.SUMMARIZATION_FUNC_MAP,
        )
        assert response == "summarize_metagpt"

    def test_select_summarize_autogen(self):
        response = agent.select_tool(
            "Summarize the autogen paper.",
            agent.SUMMARIZATION_FUNC_MAP,
        )
        assert response == "summarize_autogen"


class TestSelectHighLevelTool:

    def test_select_rag_autogen(self):
        response = agent.select_tool(
            "What is conversation programming and how does autogen use it?",
            agent.HIGH_LEVEL_FUNC_MAP,
        )
        assert response == "get_rag_map"

    def test_select_rag_metagpt(self):
        response = agent.select_tool(
            "What communication protocols are best for metagpt?",
            agent.HIGH_LEVEL_FUNC_MAP,
        )
        assert response == "get_rag_map"

    def test_select_summarize_autogen(self):
        response = agent.select_tool(
            "Summarize the autogen paper.",
            agent.HIGH_LEVEL_FUNC_MAP,
        )
        assert response == "get_summarization_map"

    def test_select_summarize_metagpt(self):
        response = agent.select_tool(
            "Summarize the metagpt paper.",
            agent.HIGH_LEVEL_FUNC_MAP,
        )
        assert response == "get_summarization_map"
