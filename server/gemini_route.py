import google.generativeai as genai
import os
from dotenv import load_dotenv

#this function uses gemini for rearangement of the prompt

def preProcessing_gemini(input: str) -> str:
    load_dotenv()
    preProcessing = """
    HERE ARE THE INSTRUCTIONS YOU NEED TO FOLLOW IN: 
    
    YOUR JOB IS TO MAKE AN EXAMPLE METHOD THAT COULD SOLVE THE GIVEN SAT PROBLEM. 
    YOU SHOULD EXPLAIN THE METHOD CLEARLY AND USING MATH, FOLLOWING THE NEXT STEPS:    

    1. EXPLAIN EACH STEP BRIEFLY AND MAKE SURE NOT TO MISS THE STEPS
    2. WHEN USING MATH TO EXPLAIN THE STEPS USE TEX, AND WRITE OUT EACH STEP
    3. MAKE SURE THE SOLUTION IS TRUE
    4. BE CONCISE AND TO THE POINT. DO NOT MAKE IT LONGER THAN IT SHOULD BE. 

    HERE IS THE PROBLEM:
    """

    GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(preProcessing, input)
    return response
