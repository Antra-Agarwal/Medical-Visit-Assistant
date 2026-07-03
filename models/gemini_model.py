import os

from dotenv import load_dotenv
from google import genai

from config import GEMINI_MODEL

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_summary(transcript):
    """
    Generates a structured medical summary using Gemini.
    """

    prompt = f"""
You are an AI Medical Assistant.

The following transcript was generated using speech-to-text and may contain small spelling mistakes.

Correct obvious spelling mistakes in medicine names if possible.

Generate a structured summary using this format:

Patient Complaint:
Diagnosis:
Medicines:
Doctor's Advice:
Follow-up:

Transcript:
{transcript}
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text

if __name__ == "__main__":

    sample_transcript = """
    Doctor, I have had a fever for three days.
    I also have a headache.
    I have been taking parasitamol.
    """

    summary = generate_summary(sample_transcript)

    print(summary)