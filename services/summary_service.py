from models.gemini_model import generate_medical_summary


def summarize_transcript(transcript):
    """
    Generate a patient-friendly medical summary.
    """

    summary = generate_medical_summary(transcript)

    return summary