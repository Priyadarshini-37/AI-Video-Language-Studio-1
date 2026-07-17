from moviepy.editor import VideoFileClip, AudioFileClip


def replace_audio(
    video_path,
    audio_path,
    output_path="final_video.mp4"
):
    """
    Replace the original video audio with new audio.
    """

    video = VideoFileClip(video_path)

    new_audio = AudioFileClip(audio_path)

    final_video = video.set_audio(new_audio)

    final_video.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac"
    )

    video.close()
    new_audio.close()

    return output_path
