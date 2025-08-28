import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_with_stop(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{user_input}"}
        ],
        stop=["END", "\n\n"],  # Stop when these sequences appear
        max_tokens=100
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    user_input = "Write a short greeting, then write END, then continue with something else."
    output = generate_with_stop(user_input)
    print("Output:\n", output)
