from utils.file_utils import save_uploaded_file
from models.whisper_model import transcribe_audio


def process_audio(uploaded_file):
    """
    Saves the uploaded audio file and converts it into text.
    """

    # Save uploaded file
    file_path = save_uploaded_file(uploaded_file)

    # Convert speech to text
    transcript = transcribe_audio(file_path)

    return file_path, transcript