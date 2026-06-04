"""Quick test to verify the Gemini API connection works."""

# Step 1: Load environment variables from the .env file
from dotenv import load_dotenv
import os

load_dotenv()  # Reads .env and makes its values available via os.getenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file. Please add it.")

# Step 2: Create a Gemini client with our API key
from google import genai
from google.genai import errors
from google.genai import types

client = genai.Client(api_key=api_key)
model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash").strip()

# Step 3: Send a focused prompt to keep the test cheap and quota-friendly
prompt = (
    "Explain relative velocity to a Class 11 student in 180-220 words. "
    "Include one simple equation and one everyday analogy."
)

config = types.GenerateContentConfig(max_output_tokens=512)
if model.startswith("gemini-2.5-flash"):
    config.thinking_config = types.ThinkingConfig(thinking_budget=0)

try:
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=config,
    )
except errors.ClientError as exc:
    if exc.code == 429:
        raise SystemExit(
            "Gemini API quota exceeded for this API key/project. "
            "Wait for the quota window to reset, enable billing, or set "
            "GEMINI_MODEL in .env to a model with available quota."
        ) from exc
    raise

# Step 4: Print the result
print(response.text)
