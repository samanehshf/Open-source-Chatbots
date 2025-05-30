# Intercat with LLM-based chatbots
input.txt              ← Input prompts (one per line)
output-*.csv           ← Output (original prompt + generated text)
models/                ← Place your .bin / .gguf model files here
generate-*.py          ← Python script for the specific model

## GPT4All Batch Text Generation

This repository contains a simple Python script for batch-generating text completions using different GPT4All models. The input is read from a text file, and the results are saved in a CSV file.

## 📁 File Structure

- `input.txt`: List of prompts (one per line)
- `output-gpt4alltest.csv`: Output CSV file containing input and generated text
- `models/`: Folder containing `.bin` model files (e.g., `ggml-gpt4all-l13b-snoozy.bin`)
- `generate.py`: Main script to run generation (this script)

---

## 🚀 How to Run

1. **Install Dependencies**

Install Python dependencies:

```bash
pip install gpt4all

## 🦙 Stanford Alpaca Batch Generation (via llama.cpp)

This script allows you to generate responses from the **Stanford Alpaca** model or any compatible `.gguf` file using the `llama.cpp` backend. Input prompts are read from `input.txt`, and generated completions are saved in `output-alpaca.csv`.

### ⚙️ Requirements

1. **Install llama.cpp**

Clone and compile the [llama.cpp](https://github.com/ggerganov/llama.cpp) repo:
```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make
