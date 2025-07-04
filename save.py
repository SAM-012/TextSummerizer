from transformers import pipeline

# This will download the model from Hugging Face and cache it
pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
print("Model downloaded and cached.")
