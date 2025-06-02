import os
import csv
import torch
from transformers import AutoTokenizer, pipeline

# Set environment variables to control CUDA device selection
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "1"  # Use GPU with index 1

# Define the model name (Falcon-7B-Instruct)
model_name = "tiiuae/falcon-7b-instruct"

# Load tokenizer for the specified model
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create a text generation pipeline using the Falcon model
generator = pipeline(
    "text-generation",
    model=model_name,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,     # Use bfloat16 for better performance on supported GPUs
    trust_remote_code=True,         # Allow custom model code from HuggingFace if needed
    device_map="auto",              # Automatically map model to available GPU(s)
)

# Open input and output files
with open('input.txt', 'r') as input_file, open('output-7B.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)

    # Process each line (prompt) from the input file
    for line in input_file:
        # Generate text using the model
        sequences = generator(
            line.strip(),
            max_length=200,        # Limit the total number of generated tokens
            do_sample=True,        # Enable sampling for more diverse output
            top_k=10,              # Limit sampling to top-k tokens
            num_return_sequences=1,  # Only one generated response per prompt
            eos_token_id=tokenizer.eos_token_id,  # Stop generation at EOS token
        )

        # Write the generated response to the output CSV
        for seq in sequences:
            csv_writer.writerow([line.strip(), seq['generated_text'].strip()])
