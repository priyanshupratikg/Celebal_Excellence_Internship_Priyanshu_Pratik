import gradio as gr

from model import generate_text


def generate(
    prompt,
    temperature,
    max_tokens
):

    return generate_text(
        prompt=prompt,
        max_new_tokens=int(max_tokens),
        temperature=temperature
    )


with gr.Blocks(
    title="Mini GPT-2 From Scratch"
) as demo:

    gr.Markdown(
        """
        # 🧠 Mini GPT-2 From Scratch

        ### A Decoder-Only Transformer Language Model

        This model was implemented and trained from scratch using PyTorch
        on the Tiny Shakespeare dataset.

        **Architecture:** 4 Transformer blocks · 4 attention heads ·
        824K parameters
        """
    )

    prompt = gr.Textbox(
        label="Prompt",
        value="ROMEO:",
        placeholder="Enter a Shakespeare-style prompt..."
    )

    temperature = gr.Slider(
        minimum=0.2,
        maximum=1.5,
        value=0.8,
        step=0.1,
        label="Temperature"
    )

    max_tokens = gr.Slider(
        minimum=50,
        maximum=1000,
        value=300,
        step=50,
        label="Maximum New Characters"
    )

    generate_button = gr.Button(
        "✨ Generate Text"
    )

    output = gr.Textbox(
        label="Generated Text",
        lines=20
    )

    generate_button.click(
        fn=generate,
        inputs=[
            prompt,
            temperature,
            max_tokens
        ],
        outputs=output
    )

    gr.Markdown(
        """
        ---
        
        **Project:** Mini GPT-2 Language Model From Scratch  
        **Framework:** PyTorch  
        **Dataset:** Tiny Shakespeare  
        **Model:** Decoder-only Transformer  

        The model achieved approximately **57.6% lower validation loss**
        compared with the Bigram baseline.
        """
    )


if __name__ == "__main__":
    demo.launch()