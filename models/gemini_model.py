import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def generate_medical_summary(transcript):

    prompt = f"""
You are an experienced medical assistant.

Read the following doctor-patient conversation.

Generate:

1. Summary
2. Medicines
3. Dosage
4. Frequency
5. Duration
6. Medical Tests
7. Follow-up Date
8. Lifestyle Advice

Use simple English suitable for senior citizens.

Transcript:

{transcript}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

if __name__ == "__main__":

    transcript = """
Patient has fever for three days.

Doctor advised Paracetamol 650 mg twice daily after meals for five days.

Drink plenty of water.

Follow up after one week.
"""

    result = generate_medical_summary(transcript)

    print(result)