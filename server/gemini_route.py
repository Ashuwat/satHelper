import google.generativeai as genai
import os
from dotenv import load_dotenv

#this function uses gemini for rearangement of the prompt
def preProcessing_gemini(input: str) -> str:
    load_dotenv()
    GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(input)
    return response

