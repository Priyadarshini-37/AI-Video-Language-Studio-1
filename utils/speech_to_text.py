import speech_recognition as sr


def speech_to_text(audio_file):
    """
    Convert audio into text.
    """

    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        return "Could not understand the audio."

    except sr.RequestError:
        return "Speech recognition service is unavailable."
