import streamlit as st
import subprocess
import pyttsx3
# Function to convert text to speech

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

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
            run_app("app.py")
    elif language == "తెలుగు":
        #speak("దయచేసి తెలుగు సంస్కరణం ఎంచుకోండి.")
        st.write("దయచేసి తెలుగు సంస్కరణం ఎంచుకోండి.")
        # Button to navigate to the Telugu version of the app
        if st.button("తెలుగు సంస్కరణంకు వెళ్ళు"):
            run_app("tapp.py")

# Call select_language function with the selected language
select_language(language)
