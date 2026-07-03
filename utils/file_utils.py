import os

from config import AUDIO_FOLDER


def save_uploaded_file(uploaded_file):
    """
    Saves the uploaded audio file and returns its path.
    """

    # Create audio folder if it doesn't exist
    os.makedirs(AUDIO_FOLDER, exist_ok=True)

    # Create full file path
    file_path = os.path.join(
        AUDIO_FOLDER,
        uploaded_file.name
    )

    # Save file
    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    return file_path