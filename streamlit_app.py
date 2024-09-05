import streamlit as st
from streamlit_mic_recorder import speech_to_text
import snowflake.connector
from snowflake.snowpark import Session

"st.session_state object:", st.session_state

if 'a_counter' not in st.session_state:
    st.session_state['a_counter'] = 0

if 'key' not in st.session_state:
    st.session_state['key'] = 0

st.write(st.session_state)

st.write(st.__version__)

# st.write("DB username:", st.secrets['user'])

conn = st.connection("snowflake")

# ACCOUNT = st.secrets["connections.snowflake"]["account"]

# Create a Snowflake session
# def create_session():
#  connection_parameters = st.secrets["connections.snowflake"]
#  session = Session.builder.configs(connection_parameters).create()
#   return session

# session = create_session()
# st.success("Connected to Snowflake!")

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

details_val = st.session_state.my_stt_output
st.write(details_val)
