import csv
import subprocess

# Path to LLaMA binary compiled from llama.cpp
LLAMA_BINARY_PATH = "./llama.cpp/main"

# Path to your GGUF-format model (e.g., Stanford Alpaca converted to .gguf)
MODEL_PATH = "./models/alpaca-7b.gguf"

# Maximum number of tokens to generate
MAX_TOKENS = 55

# Number of GPU layers to offload (use 0 if no GPU)
NUM_GPU_LAYERS = 32

# Input and output file paths
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output-alpaca.csv"

# Open input file and output CSV
with open(INPUT_FILE, "r", encoding="utf-8") as infile, open(OUTPUT_FILE, "w", newline='', encoding="utf-8") as outfile:
    csv_writer = csv.writer(outfile)

    # Process each line (prompt) from input
    for idx, prompt in enumerate(infile):
        prompt = prompt.strip()  # Remove leading/trailing whitespace

        if not prompt:
            continue  # Skip empty lines

        print(f"[{idx+1}] Generating for prompt: {prompt[:60]}...")

        # Build the command for llama.cpp model execution
        cmd = [
            LLAMA_BINARY_PATH,
            "-m", MODEL_PATH,
            "-f", "-",                # Read prompt from stdin
            "-n", str(MAX_TOKENS),   # Number of tokens to generate
            "-ngl", str(NUM_GPU_LAYERS)
        ]

        # Run the model and feed prompt via stdin
        result = subprocess.run(cmd, input=prompt.encode("utf-8"), capture_output=True)

        # Extract output text
        output_text = result.stdout.decode("utf-8", errors="ignore").strip()

        # Write to CSV: [Prompt, Response]
        csv_writer.writerow([prompt, output_text])
