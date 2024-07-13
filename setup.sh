#!/bin/bash

set -e

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Install Ollama model
ollama run mistral
ollama run nomic-embed-text

# Install dependencies
pip install -r requirements.txt