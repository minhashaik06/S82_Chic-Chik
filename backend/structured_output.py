import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Example: Structured Output for a simple task
def get_structured_output(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Extract structured details from: {user_input}"}
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "extracted_info",
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "age": {"type": "integer"},
                        "city": {"type": "string"}
                    },
                    "required": ["name", "age", "city"]
                }
            }
        }
    )

    return response.choices[0].message

if __name__ == "__main__":
    user_input = "Hi, I’m Alex, 25 years old, living in Bangalore."
    structured_data = get_structured_output(user_input)
    print("Structured Output:\n", structured_data)
