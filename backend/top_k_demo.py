import os
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load a small open-source model (for demo purpose)
model_name = "gpt2"   # lightweight
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_with_top_k(prompt, k=50, max_length=50):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=max_length,
        do_sample=True,
        top_k=k,        # 👈 Top-K parameter
        top_p=1.0,      # disable nucleus sampling
        temperature=1.0
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage
prompt = "Suggest three stylish outfit ideas for a weekend brunch."
print("AI Reply:\n", generate_with_top_k(prompt, k=40))
