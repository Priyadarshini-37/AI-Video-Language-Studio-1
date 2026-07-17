from moviepy.editor import VideoFileClip


def extract_audio(video_path, audio_path="extracted_audio.wav"):
    video = VideoFileClip(video_path)

    if video.audio is None:
        video.close()
        raise ValueError("The video does not contain audio.")

    video.audio.write_audiofile(audio_path)

    video.close()

    return audio_path
