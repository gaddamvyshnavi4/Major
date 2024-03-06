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
g = gTTS( "Please provide the following details for crop yield prediction.",lang='en-uk', slow=False)
g.save("eintro.mp3")
playsound("eintro.mp3")
os.remove('eintro.mp3')