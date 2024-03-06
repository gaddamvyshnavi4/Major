import os
from gtts import gTTS
import base64
import streamlit as st
import pickle
import numpy as np

from io import BytesIO
import playsound

from playsound import playsound
from gtts import gTTS
def speak(text):
    tts = gTTS(text=text, lang='en')
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    audio_bytes = mp3_fp.getvalue()
    audio_b64 = base64.b64encode(audio_bytes).decode()
    audio_html = f'<audio autoplay="autoplay" controls="controls" style="width: 100%; max-width: 500px;"><source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3" /></audio>'
    st.markdown(audio_html, unsafe_allow_html=True)

speak("Predicted Production ")