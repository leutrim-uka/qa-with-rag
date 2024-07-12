# Question-Answering with RAG
Implementation of question answering on PDF files using Retrieval Augmented Generation. 

## Setup
Since this project will work locally, you need to install Ollama first. You can do so from the official website [here](https://ollama.com/). Once the installation is complete, make sure the Ollama server is running.

From the terminal, use the following command to download the language model, on which your LLM app will be based:
```{bash}
ollama run <model-name>
```
Replace _<model_name>_ with an actual model name from the [official list](https://ollama.com/library).


