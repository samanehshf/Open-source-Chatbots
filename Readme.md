# Intercat with LLM-based chatbots
input.txt              ← Input prompts (one per line)
output-*.csv           ← Output (original prompt + generated text)
models/                ← Place your .bin / .gguf model files here
generate-*.py          ← Python script for the specific model
This repository contains a simple Python script for batch-generating text completions using different GPT4All models. The input is read from a text file, and the results are saved in a CSV file.

🤖 GPT4All Batch Text Generation

This script uses the official `gpt4all` Python package to load a local `.bin` model and generate responses for each line in an input text file. The outputs are saved to a CSV file in `[Prompt, Response]` format.

⚙️ Requirements

1. **Install Python Package**

You can install the GPT4All Python interface with:
```bash
pip install gpt4all
****************************************************************************************************************************************************************# 🦙 Stanford Alpaca Batch Generation (via llama.cpp)

This script allows you to generate responses from the **Stanford Alpaca** model or any compatible `.gguf` file using the `llama.cpp` backend. Input prompts are read from `input.txt`, and generated completions are saved in `output-alpaca.csv`.

⚙️ Requirements

1. **Install llama.cpp**


Clone and compile the [llama.cpp](https://github.com/ggerganov/llama.cpp) repo:
```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make
