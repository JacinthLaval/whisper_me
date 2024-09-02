import streamlit as st
from streamlit_mic_recorder import speech_to_text

def callback():
    if st.session_state.my_stt_output:
        st.write(st.session_state.my_stt_output)

# Set up the speech-to-text component
speech_to_text(
    language='en',  # Specify the language for speech recognition
    start_prompt="Start recording",
    stop_prompt="Stop recording",
    key='my_stt',
    callback=callback
)
