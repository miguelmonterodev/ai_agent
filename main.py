import os
from dotenv import load_dotenv
from google import genai
import sys

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# accept a command line argument for the prompt.
try:
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=sys.argv[1])
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print("Response tokens: ")#response.usage_metadata.candidates_token_count
except IndexError:
    print("Error: we need argument as an input. Example: uv run main.py 'input'")
    