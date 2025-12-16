# chat-agent

### Overview

The Chat-Agent system is designed to execute GPT queries using intelligent tool selection. It leverages a hierarchical approach, dynamically choosing between summarization and Retrieval-Augmented Generation (RAG) tools, further refined to specific implementations within each category.

### System Components

- **Function Maps**: Two primary mappings, `SUMMARIZATION_FUNC_MAP` and `RAG_FUNC_MAP`, direct the system to the appropriate processing function based on query characteristics.
- **Tool Builder**: Constructs tool objects for the completions API, enabling dynamic function selection through GPT-4-Turbo completions.
- **Tool Selection**: Utilizes OpenAI's API to select the optimal tool for query execution, based on the system-generated context and the user's query.

### Operation

1. **Initialization**: The system categorizes the query as either requiring summarization or RAG, based on predefined logic and tool mappings.
2. **Tool Selection**: Through the `select_tool` function, it determines the specific tool (e.g., `rag_metagpt`, `rag_autogen`, etc.) that best suits the query.
3. **Execution**: The selected tool processes the query, with the outcome logged for transparency and debugging purposes.


# Development

### setup environment and run demo
```bash
virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

export OPENAI_API_KEY=your-api-key

python src/demo.py
```

### Run tests
```bash
pip install -r requirements.dev.txt

pytest
```


---
Last updated: 2026-02-23 13:47:02
