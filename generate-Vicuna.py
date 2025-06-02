from llama_cpp import Llama
import csv

# Initialize the quantized Vicuna 13B model (4-bit version)
# Make sure the corresponding .bin model file is present in the working directory
llm = Llama(model_path="ggml-vicuna-13b-4bit-rev1.bin")

print("Model loaded successfully. Starting inference...")

# Open input and output files
with open('input.txt', 'r') as input_file, open('output-vicuna-13b-4bit.csv', 'w', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    count = 0  # Counter to track processed lines

    # Process each line (question) from the input file
    for line in input_file:
        count += 1
        print(f"Processing line {count}")

        # Format the input prompt for the model
        prompt = f"Question: {line.strip()} Answer:"
        answer = ""

        # Retry if model returns an empty response (ensures at least some text is generated)
        while len(answer.strip()) < 4:
            stream = llm(
                prompt,
                max_tokens=512,  # Maximum number of tokens to generate
                stop=["\n", "Question:", "Q:"],  # Stop generation at these tokens
                stream=True,  # Streaming response
            )
            output = next(stream)  # Fetch first streamed output
            answer = output["choices"][0]["text"]

        # Write the input question and generated answer to CSV
        csv_writer.writerow([line.strip(), answer.strip()])
