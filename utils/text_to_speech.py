from gtts import gTTS


def text_to_speech(
    text,
    language="en",
    output_file="generated_voice.mp3"
):
    """
    Convert text into speech.
    """

    speech = gTTS(
        text=text,
        lang=language
    )

    speech.save(output_file)

    return output_file
