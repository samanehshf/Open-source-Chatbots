![image](https://github.com/user-attachments/assets/68351c36-688b-4482-9657-de8777a5967b)# Intercat with LLM-based chatbots
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
****************************************************************************************************************************************************************
 🦙 Stanford Alpaca Batch Generation (via llama.cpp)

This script allows you to generate responses from the **Stanford Alpaca** model or any compatible `.gguf` file using the `llama.cpp` backend. Input prompts are read from `input.txt`, and generated completions are saved in `output-alpaca.csv`.

⚙️ Requirements

1. **Install llama.cpp**


Clone and compile the [llama.cpp](https://github.com/ggerganov/llama.cpp) repo:
```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make
**************************************************************************************************************************************************************
🦙 Vicuna 13B Batch Generation (via llama.cpp)
This script uses the Vicuna 13B 4-bit quantized model through the llama.cpp backend to generate answers for each prompt provided in an input text file. It's optimized for local inference on consumer GPUs or CPUs using quantized .bin files.

📥 Input & Output
Input File: input.txt — Each line is treated as a new question.

Output File: output-vicuna-13b-4bit.csv — Each row contains a [Prompt, Response] pair.

⚙️ Requirements
Install llama.cpp
******************************************************************************************************************************************************************
🦅 Falcon 7B Instruct Batch Generation (via HuggingFace Transformers)

This script uses the Falcon-7B-Instruct model from TII UAE through the HuggingFace transformers pipeline to generate responses for each prompt in an input text file. It supports fast local inference using GPU with bfloat16 precision.

📥 Input & Output

Input File: input.txt — Each line is treated as a separate prompt.

Output File: output-7B.csv — Each row contains a [Prompt, Response] pair.

⚙️ Requirements

Install Required Packages
pip install transformers accelerate

****************************************************************************************************************************************************************

Citation:
@article{shafee2024evaluation,
  title={Evaluation of LLM-based chatbots for OSINT-based Cyber Threat Awareness},
  author={Shafee, Samaneh and Bessani, Alysson and Ferreira, Pedro M},
  journal={Expert Systems with Applications},
  pages={125509},
  year={2024},
  publisher={Elsevier}
}


