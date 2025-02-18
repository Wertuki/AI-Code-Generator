import openai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

def generate_code(prompt):
    """Generates Python code based on user input using OpenAI GPT API."""
    openai.api_key = API_KEY

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Generate Python code based on this prompt:"},
                  {"role": "user", "content": prompt}],
        max_tokens=200
    )

    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    user_prompt = input("Describe the code you need: ")
    result = generate_code(user_prompt)
    print("\nGenerated Code:\n", result)
