import pysrt


def create_subtitle(text, output_file="subtitle.srt"):
    """
    Create a basic subtitle file.
    """

    subtitles = pysrt.SubRipFile()

    subtitle = pysrt.SubRipItem(
        index=1,
        start=pysrt.SubRipTime(seconds=0),
        end=pysrt.SubRipTime(seconds=10),
        text=text
    )

    subtitles.append(subtitle)

    subtitles.save(output_file)

    return output_file
