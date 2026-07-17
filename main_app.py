import streamlit as st

from utils.extract_audio import extract_audio
from utils.speech_to_text import speech_to_text
from utils.translate import translate_text
from utils.text_to_speech import text_to_speech


st.set_page_config(
    page_title="AI Video Language Studio",
    page_icon="🎬"
)

st.title("🎬 AI Video Language Studio")

st.write(
    "Upload a video and translate its speech into another language."
)


uploaded_file = st.file_uploader(
    "📤 Upload your video",
    type=["mp4", "mov", "avi", "mkv"]
)


language_names = {
    "English": "en",
    "Kannada": "kn",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te"
}


selected_language = st.selectbox(
    "🌍 Select target language",
    list(language_names.keys())
)


target_language = language_names[selected_language]


if uploaded_file is not None:

    input_video = "input_video.mp4"

    with open(input_video, "wb") as file:
        file.write(uploaded_file.read())

    st.success("✅ Video uploaded successfully!")

    st.video(input_video)


    if st.button("🚀 Start Processing"):

        try:

            # STEP 1: Extract audio
            with st.spinner("🎵 Extracting audio..."):

                audio_file = extract_audio(
                    input_video
                )

            st.success("✅ Audio extracted successfully!")


            # STEP 2: Speech to text
            with st.spinner("🤖 Converting speech to text..."):

                original_text = speech_to_text(
                    audio_file
                )

            st.subheader("📝 Original Transcript")

            st.write(original_text)


            # STEP 3: Translate
            with st.spinner(
                f"🌍 Translating to {selected_language}..."
            ):

                translated_text = translate_text(
                    original_text,
                    target_language
                )

            st.success("✅ Translation completed!")

            st.subheader(
                f"🌍 Translated Text ({selected_language})"
            )

            st.write(translated_text)


            # STEP 4: Text to speech
            with st.spinner("🔊 Generating voice..."):

                voice_file = text_to_speech(
                    translated_text,
                    target_language
                )

            st.success("✅ Voice generated!")

            st.audio(voice_file)

            with open(voice_file, "rb") as file:

                st.download_button(
                    label="⬇️ Download Translated Audio",
                    data=file,
                    file_name="translated_voice.mp3",
                    mime="audio/mpeg"
                )


        except Exception as error:

            st.error(
                f"❌ Error occurred: {error}"
            )
