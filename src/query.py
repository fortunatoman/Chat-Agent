import fitz
from llama_index import (
    SimpleDirectoryReader,
    VectorStoreIndex,
)
from llama_index.llms import OpenAI


def rag_query(input_dir: str, query: str) -> str:
    """Build rag pipeline on source documents and execute query."""
    reader = SimpleDirectoryReader(input_dir, recursive=True)
    documents = reader.load_data()
    index = VectorStoreIndex.from_documents(documents)
    return index.as_query_engine().query(query).response


def summarization_query(pdf_path: str, query: str) -> str:
    """Send entire document to query engine for summarization."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return OpenAI().complete(query).text
