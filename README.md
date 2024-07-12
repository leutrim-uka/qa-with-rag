# Question-Answering with RAG
Implementation of question answering on PDF files using Retrieval Augmented Generation. 

## Setup

### Running Ollama locally
Since this project will work locally, you need to install Ollama first. You can do so from the official website [here](https://ollama.com/). Once the installation is complete, make sure the Ollama server is running.

From the terminal, use the following command to download the language model, on which your LLM app will be based:
```{bash}
ollama run <model-name>
```
Replace _<model_name>_ with an actual model name from the [official list](https://ollama.com/library).

### Install dependencies
As usual, run the following command to install Python dependencies:
```{bash}
pip install -r requirements.txt
```

## Running the app
Until I can find the time to build a frontend, the app should be ran from the terminal.
1. Add PDF files to the `data` folder
2. Change the directory: `cd ./src`
3. Run the following:
```{bash}
python query_data.py "<Question about PDF content here>"
```

## Embeddings
The quality of the answers depends a lot on the embedding model you use. You can use embedding models from Ollama, or through the `langchain-huggingface` library. Based on experience, models like `all-MiniLM-L6-v2` prevent Mistral from answering any questions, whereas models like `nomic-embed-text` show noticeable improvements. If you have access to APIs from OpenAPI or Amazon, they might work even better than the local ones.
