from gtts import gTTS
import base64
import streamlit as st
import pickle
import numpy as np
import pyttsx3
from io import BytesIO
import streamlit as st
import subprocess
import pyttsx3
# Function to convert text to speech

#engine = pyttsx3.init()
#def speak(text):
#    engine.say(text)
#    engine.runAndWait()

# Function to run the Streamlit app with subprocess
def run_app(app_name):
    subprocess.Popen(["streamlit", "run", app_name])

# Landing page content
st.title("Welcome to Crop Yield Prediction App")

# Prompt to select language
st.write("Please select your preferred language:")
language = st.radio("", ("English", "తెలుగు"))  # Translate "తెలుగు" to Telugu

# Function to handle language selection
def select_language(language):
    if language == "English":
        #speak("Please select the English version of the app.")
        st.write("Please select the English version of the app.")
        # Button to navigate to the English version of the app
        if st.button("Go to English version"):
            pickled_model=pickle.load(open('dtr1.pkl','rb'))
            f=pickle.load(open('preprocessor1.pkl','rb'))
            def speak(text):
                tts = gTTS(text=text, lang='te')
                mp3_fp = BytesIO()
                tts.write_to_fp(mp3_fp)
                audio_bytes = mp3_fp.getvalue()
                audio_b64 = base64.b64encode(audio_bytes).decode()
                audio_html = f'<audio autoplay="autoplay" controls="controls" style="width:100%"><source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3" /></audio>'
                st.markdown(audio_html, unsafe_allow_html=True)

            
    elif language == "తెలుగు":
        #speak("దయచేసి తెలుగు సంస్కరణం ఎంచుకోండి.")
        st.write("దయచేసి తెలుగు సంస్కరణం ఎంచుకోండి.")
        # Button to navigate to the Telugu version of the app
        if st.button("తెలుగు సంస్కరణంకు వెళ్ళు"):
            #run_app("tapp.py")
            pass

# Call select_language function with the selected language
select_language(language)
