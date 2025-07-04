import torch
import gradio as gr
from transformers import pipeline

# Define the path to your local model (use raw string for Windows path)

# Create summarization pipeline using local model
text_summary = pipeline(
    "summarization",
    model=sshleifer/distilbart-cnn-12-6,
    torch_dtype=torch.bfloat16
)

# Define the summarization function
def summary(input_text):
    output = text_summary(input_text)
    return output[0]['summary_text']

# Close any existing Gradio demos
gr.close_all()

# Create Gradio Interface
demo = gr.Interface(
    fn=summary,
    inputs=gr.Textbox(label="Input text to summarize", lines=6),
    outputs=gr.Textbox(label="Summarized text", lines=4),
    title="@GenAILearniverse Project 1: Text Summarizer",
    description="THIS APPLICATION WILL BE USED TO SUMMARIZE THE TEXT"
)

demo.launch()
