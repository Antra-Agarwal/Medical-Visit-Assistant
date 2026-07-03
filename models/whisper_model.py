from faster_whisper import WhisperModel

from config import WHISPER_MODEL


# Load the Whisper model only once
whisper = WhisperModel(
    WHISPER_MODEL,
    device="cpu",
    compute_type="int8"
)


def transcribe_audio(audio_path):
    """
    Converts an audio file into text.
    """

    segments, info = whisper.transcribe(audio_path)

    transcript = ""

    for segment in segments:
        transcript += segment.text + " "

    return transcript.strip()

if __name__ == "__main__":

    transcript = transcribe_audio("audio/Sample.wav")

    print(transcript)