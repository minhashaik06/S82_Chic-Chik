import os
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("GEMINI_API_KEY environment variable not set.")

genai.configure(api_key=api_key)

prompt = """

You are an expert Python programmer. 
Task: Write a Python function to check whether a given string is a palindrome. 
Requirements:
- Use a clean and efficient solution.
- Include comments in the code for clarity.
- Output only the code (no explanations).
"""



model = genai.GenerativeModel('gemini-pro')
try:
    response = model.generate_content(prompt)
    print(response.text.strip())
except Exception as e:
    print(f"Error generating content: {e}")