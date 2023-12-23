# Install Text Generation WebUI
import gradio as gr
from transformers import *
import torch

theme = gr.themes.Monochrome(
    primary_hue="indigo",
    secondary_hue="blue",
    neutral_hue="slate",
    radius_size=gr.themes.sizes.radius_sm,
    font=[gr.themes.GoogleFont("Open Sans"),
          "ui-sans-serif", "system-ui", "sans-serif"],
)
model_name = "/home/sshafee/dolly-v2-12b"
# model_name = "F:/Dolly 2.0/dolly-v2-7b"
tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left")
# model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype=torch.bfloat16, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name, device_map="auto", load_in_8bit=True, trust_remote_code=True)

end_key_token_id = tokenizer.encode("### End")[0]

instruct_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer,
                             pad_token_id=tokenizer.pad_token_id, eos_token_id=end_key_token_id)


def generate(instruction):
    input_ids = tokenizer.encode(instruction, return_tensors="pt")
    # Move input_ids to the same device as the model
    input_ids = input_ids.to(model.device)
    generated_output = model.generate(
        input_ids, max_length=256, pad_token_id=tokenizer.pad_token_id, eos_token_id=end_key_token_id)
    dd = tokenizer.decode(generated_output[0])
    return dd


examples = [
    "Instead of making a peanut butter and jelly sandwich, what else could I combine peanut butter with in a sandwich? Give five ideas",
    "How do I make a campfire?",
    "Write me a tweet about the release of Dolly 2.0, a new LLM"
]


def process_example(args):
    for x in generate(args):
        pass
    return x


css = ".generating {visibility: hidden}"

with gr.Blocks(theme=theme, analytics_enabled=False, css=css) as demo:
    with gr.Column():
        gr.Markdown(
            """ ## Dolly 2.0
            Dolly 2.0 is a 12B parameter language model based on the EleutherAI pythia model family and fine-tuned exclusively on a new, high-quality human generated instruction following dataset, crowdsourced among Databricks employees. For more details, please refer to the [model card](https://huggingface.co/databricks/dolly-v2-12b)
            
            Type in the box below and click the button to generate answers to your most pressing questions!
            
      """
        )
        gr.HTML("<p>Check out SECourses for AI, Stable Diffusion, ML and Programming Related Full Free Courses, Tutorials and Guides  : <a target='_blank' style='display:inline-block' href='https://www.youtube.com/@SECourses' alt='https://www.youtube.com/@SECourses'>https://www.youtube.com/@SECourses</a> </p>")

        with gr.Row():
            with gr.Column(scale=3):
                instruction = gr.Textbox(
                    placeholder="Is the sentence 'smartshop 1 sql injection packetstorm' related to cyber security? Just answer yes or no.", label="Question", elem_id="q-input")

                with gr.Box():
                    gr.Markdown("**Answer**")
                    output = gr.Markdown(elem_id="q-output")
                submit = gr.Button("Generate", variant="primary")
                gr.Examples(
                    examples=examples,
                    inputs=[instruction],
                    cache_examples=False,
                    fn=process_example,
                    outputs=[output],
                )

    submit.click(generate, inputs=[instruction], outputs=[output])
    instruction.submit(generate, inputs=[instruction], outputs=[output])

demo.queue(concurrency_count=1).launch(debug=True)
