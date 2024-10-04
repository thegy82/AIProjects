import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key)

# Create a chat completion
completions = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a haiku about recursion in programming."}
    ]
)

# Print the response
print(completions.choices[0].message.content)
