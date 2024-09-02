pip install openai-whisper

import streamlit as st
import whisper

@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")

st.title("Whisper Speech Recognition")

uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "m4a"])
transcribe_button = st.button("Transcribe Audio")

if transcribe_button and uploaded_file is not None:
    model = load_whisper_model()
    
    # Save the uploaded file temporarily
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Transcribe the audio
    result = model.transcribe("temp_audio.wav")
    
    # Display the transcription
    st.write("Transcription:")
    st.write(result["text"])
