import os
from openai import OpenAI
import tiktoken

# Load API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def count_tokens(text, model="gpt-4o-mini"):
    """Utility to count tokens using tiktoken"""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

# Example prompt
prompt = "Suggest three stylish outfit ideas for a weekend brunch."

# Call OpenAI with top_p parameter
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=200,
    temperature=0.7,
    top_p=0.8   # 👈 Added Top-P (nucleus sampling)
)

reply = response.choices[0].message.content
print("AI Reply:\n", reply)

# Log token usage
total_tokens = response.usage.total_tokens
print(f"\n[Token Usage] Total: {total_tokens} tokens")
