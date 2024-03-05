import os
import streamlit as st
from streamlit_option_menu import option_menu
import pygame

import os
from gtts import gTTS
import base64
import streamlit as st
import pickle
import numpy as np
import pyttsx3
from io import BytesIO
import playsound

from playsound import playsound
from gtts import gTTS

    # Streamlit UI
st.title('Crop Yield Prediction')

def get_state():
        return st.session_state

if 'message_spoken' not in get_state():
        
        get_state().message_spoken = {'intro': False, 'state': False, 'district': False,
                                      'season': False, 'crop': False, 'area': False, 'temperature': False,
                                      'wind_speed': False, 'precipitation': False,
                                      'humidity': False, 'soil_type': False, 'prediction': False}

    # Speak the message for introduction if it hasn't been spoken before
if not get_state().message_spoken['intro']:
        tts = gTTS("Please provide the following details for crop yield prediction.", lang='en-uk', slow=False)
        tmp_file_name = "eintro.mp3"
        tts.save(tmp_file_name)
        pygame.mixer.init()
        pygame.mixer.music.load(tmp_file_name)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue  # Wait for the audio to finish playing
        os.remove(tmp_file_name)
        get_state().message_spoken['intro'] = True
