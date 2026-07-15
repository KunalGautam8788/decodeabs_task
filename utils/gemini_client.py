import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API Key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load Model
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash"
)

def get_response(prompt):
    """
    Generate response from Gemini model.
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"