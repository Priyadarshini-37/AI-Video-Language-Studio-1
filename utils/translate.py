from deep_translator import GoogleTranslator


def translate_text(text, target_language):
    """
    Translate text into the selected language.
    """

    translated = GoogleTranslator(
        source="auto",
        target=target_language
    ).translate(text)

    return translated
