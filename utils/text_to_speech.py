import whisper
import text_to_speech

def speech_to_text(audio_file):
    """
    Convert audio into text using Whisper AI.
    """

    model = whisper.load_model("base")

    result = model.transcribe(
        audio_file
    )

    return result["text"]
