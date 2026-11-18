from google import genai
from google.genai import types

MODEL_NAME = "gemini-3.5-flash-lite"

SYSTEM_INSTRUCTION = """
You are AI Helper, an expert mathematical tutor.

Solve real-life mathematics problems in simple, student-friendly English.

Use these sections where relevant:
1. Understanding the Problem
2. Mathematical Concept
3. Given Information
4. Mathematical Model
5. Step-by-Step Solution
6. Final Answer
7. Real-Life Meaning
8. Try This

Show formulas, calculations and units.
Never invent missing measurements.
State assumptions clearly.
Keep explanations clear and focused. Avoid unnecessary lengthy introductions.
"""

def solve_real_life_problem(question, api_key):
    if not question or not question.strip():
        return "Please enter a question first."

    if not api_key:
        return "Gemini API key is missing."

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=question.strip(),
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                temperature=0.2,
                max_output_tokens=1200,
            ),
        )

        if response.text:
            return response.text

        return "The AI returned an empty response. Please try again."

    except Exception as error:
        print(f"Gemini request error: {error}")
        return (
            "AI Helper could not get a response right now. "
            "Please check your internet connection and try again."
        )
