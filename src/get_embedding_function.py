"""
This module can be used to experiment with different embedding models. The
current setup requires Ollama to be installed and running, so that the app
can establish a connection.

The main function in this module is `get_embedding_function`, which returns
an instance of the OllamaEmbeddings model.

Note: If you have access to OpenAI or AWS APIs for generating embeddings,
they will most likely work better than the local version
"""

from langchain_community.embeddings.ollama import OllamaEmbeddings

# from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_function():
    """
    Initializes and returns the selected embedding model. Designed to be used
    with the embed_query method.

    Returns:
        Initialized embedding model for embedding generation and querying
    """
    # embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
