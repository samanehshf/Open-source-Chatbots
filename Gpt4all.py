import csv
from gpt4all import GPT4All

# Counter to track how many lines have been processed
line_counter = 0

# Open input and output files
with open('input.txt', 'r') as input_file, open('output-gpt4alltest.csv', 'w', newline='', encoding='utf-8') as output_file:
    
    # Initialize GPT4All model
    # Note: Avoid setting `n_ctx` too high. Exceeding context memory can cause a segmentation fault.
    # Example of error when `n_ctx` is too high:
    # ggml_new_tensor_impl: not enough space in the context's memory pool (needed 18... , available ...)
    model = GPT4All('./models/ggml-gpt4all-l13b-snoozy.bin', n_ctx=512)
    
    # Initialize CSV writer
    csv_writer = csv.writer(output_file)
    
    # Process each line in the input file
    for line in input_file:
        # Generate a response using the model (limit to 55 tokens)
        result = model.generate(line.strip(), n_predict=55)

        # Join list of tokens into a single string
        generated_text = ''.join(result)
        
        # Increment and display line counter
        line_counter += 1
        print(f"Processed line: {line_counter}")
        
        # Write input + generated output to CSV
        csv_writer.writerow([line.strip(), generated_text])
