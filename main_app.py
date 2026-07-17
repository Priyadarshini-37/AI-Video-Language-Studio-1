import streamlit as st

from utils.extract_audio import extract_audio
from utils.speech_to_text import speech_to_text
from utils.translate import translate_text
from utils.text_to_speech import text_to_speech


# Page settings
st.set_page_config(
    page_title="AI Video Language Studio",
    page_icon="🎬",
    layout="wide"
)


# Title
st.title("🎬 AI Video Language Studio")

st.write(
    "Upload a video, convert speech into text, "
    "translate it into another language, and generate voice."
)


# Upload video
uploaded_file = st.file_uploader(
    "📤 Upload your video",
    type=["mp4", "mov", "avi", "mkv"]
)


if uploaded_file is not None:

    # Save uploaded video
    input_video = "input_video.mp4"

    with open(input_video, "wb") as file:
        file.write(uploaded_file.read())

    st.success("✅ Video uploaded successfully!")

    # Display video
    st.video(input_video)


    # Process video
    if st.button("🚀 Start Processing"):

        try:

            # Extract audio
            with st.spinner("🎵 Extracting audio..."):

                audio_file = extract_audio(
                    input_video
                )

            st.success("✅ Audio extracted successfully!")


            # Speech to text
            with st.spinner("📝 Converting speech to text..."):

                original_text = speech_to_text(
                    audio_file
                )

            st.subheader("📝 Original Transcript")

            st.write(original_text)


            # Language selection
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


            target_language = language_names[
                selected_language
            ]


            # Translate
            if st.button("🌐 Translate Text"):

                with st.spinner("Translating..."):

                    translated_text = translate_text(
                        original_text,
                        target_language
                    )

                st.subheader("🌍 Translated Text")

                st.write(translated_text)


                # Generate voice
                if st.button("🔊 Generate Voice"):

                    with st.spinner(
                        "Generating voice..."
                    ):

                        voice_file = text_to_speech(
                            translated_text,
                            target_language
                        )

                    st.success(
                        "✅ Voice generated successfully!"
                    )

                    st.audio(voice_file)


                    # Download voice
                    with open(
                        voice_file,
                        "rb"
                    ) as file:

                        st.download_button(
                            label="⬇️ Download Voice",
                            data=file,
                            file_name="translated_voice.mp3",
                            mime="audio/mpeg"
                        )


        except Exception as error:

            st.error(
                f"❌ Error: {error}"
            )
