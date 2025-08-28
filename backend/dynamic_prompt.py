import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Dynamic variables
language = "Python"
task = "Write a function to check if a number is prime."

# Prompt template
prompt = f"""
You are a helpful coding assistant.  
Task: Based on the provided programming language and task, generate an efficient solution.  
Requirements:
- Write clean, optimized code.
- Add comments for clarity.
- Return only the code (no extra text).  

Language: {language}  
Task: {task}  
"""

# New API call
response = client.chat.completions.create(
    model="gpt-4o-mini",   # or "gpt-4.1-mini" etc.
    messages=[{"role": "user", "content": prompt}],
    max_tokens=300,
    temperature=0.2
)

print(response.choices[0].message.content.strip())
