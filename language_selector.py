from gtts import gTTS
import base64
import streamlit as st
import pickle
import numpy as np
import pyttsx3
import time
import streamlit as st
import pickle
import numpy as np
from gtts import gTTS
from io import BytesIO
import base64
def delay():
                x = 0
                for _ in range(10**7):
                    x += 1
# Load the model
# Save the DecisionTreeRegressor model to a pickle file
# Load the preprocessor and model from pickle files

pickled_model = pickle.load(open('dtr1.pkl','rb'))
f = pickle.load(open('preprocessor1.pkl','rb'))
import base64
from streamlit_option_menu import option_menu
from gtts import gTTS
from io import BytesIO
import streamlit as st
selected=option_menu(
    menu_title=None,
    options=["Home ","English","తెలుగు"],
    icons=["house","alphabet-uppercase",""],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)
def speak1(text):
    tts = gTTS(text=text, lang='te')
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    audio_bytes = mp3_fp.getvalue()
    audio_b64 = base64.b64encode(audio_bytes).decode()
    audio_html = f'<audio autoplay="autoplay" controls="controls" style="width:100%"><source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3" /></audio>'
    st.markdown(audio_html, unsafe_allow_html=True)
    audio_length = len(audio_bytes) / 1000  # Calculate audio length in seconds
    return audio_length

# Example usage:

# Prediction function
def predict_production(state_names, district_names, season_names, crop_names, area, temperature, wind_speed, precipitation, humidity, soil_type):
    # Create an array of the input features
    features = np.array([[state_names, district_names, season_names, crop_names, area, temperature, wind_speed, precipitation, humidity, soil_type]], dtype=object)
    # Transform the features using the preprocessor
    transformed_features = f.transform(features)
    # Make the prediction using the trained model
    predicted_production = pickled_model.predict(transformed_features).reshape(1, -1)
    return predicted_production[0]

# Streamlit UI
st.title('Crop Yield Prediction')

# Initialize pyttsx3 Engine
message_spoken = False
# Function to convert text to speech

def get_state():
    return st.session_state
if selected=="English":
    
    if 'message_spoken' not in get_state():
        get_state().message_spoken = {'intro': False,'state': False, 'district': False, 
                                    'season': False,'crop': False, 'area': False, 'temperature': False,
                                    'wind_speed': False, 'precipitation': False,
                                    'humidity': False, 'soil_type': False,'prediction':False}

    # Speak the message for introduction if it hasn't been spoken before
    if not get_state().message_spoken['intro']:
        delay1=speak1("Please provide the following details for crop yield prediction.")
        if delay1:
            # Define a function that performs a series of simple calculations
            

            # Execute the function to simulate a delay
            delay()
            delay()
            delay()
            delay()
            delay()
            delay()
            delay()
            delay()
            delay()
            delay()
            delay()
            delay()
            delay()


            pass
        else:
            st.write("Error: Could not get duration for audio clip")
        get_state().message_spoken['intro'] = True

    # Speak the message for state names if it hasn't been spoken before
    state_names_options = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh']
    state_names = st.selectbox('Select State Name', state_names_options)
    if not get_state().message_spoken['state']:
        delay1=speak1("state for crop yield prediction.")
        if delay1:
            delay()
            delay()
            delay()
            delay()
            delay()
            delay()
            delay()

        get_state().message_spoken['state'] = True

    districts_by_state = {'Andaman and Nicobar Islands': ['NICOBARS', 'NORTH AND MIDDLE ANDAMAN', 'SOUTH ANDAMANS'], 'Andhra Pradesh': ['ANANTAPUR', 'CHITTOOR', 'EAST GODAVARI', 'GUNTUR', 'KADAPA', 'KRISHNA', 'KURNOOL', 'PRAKASAM', 'SPSR NELLORE', 'SRIKAKULAM', 'VISAKHAPATANAM', 'VIZIANAGARAM', 'WEST GODAVARI'], 'Arunachal Pradesh': ['ANJAW', 'CHANGLANG', 'DIBANG VALLEY', 'EAST KAMENG', 'EAST SIANG', 'KURUNG KUMEY', 'LOHIT', 'LONGDING', 'LOWER DIBANG VALLEY', 'LOWER SUBANSIRI', 'NAMSAI', 'PAPUM PARE', 'TAWANG', 'TIRAP', 'UPPER SIANG', 'UPPER SUBANSIRI', 'WEST KAMENG', 'WEST SIANG']}

    if state_names:
        district_names = st.selectbox('Select District', districts_by_state[state_names])
    if not get_state().message_spoken['district']:
        delay1=speak1("district for crop yield prediction.")
        if delay1:
            delay()
            delay()
            delay()
            delay()
            delay()
            delay()
            delay()

        get_state().message_spoken['district'] = True
    season = ['Kharif', 'Whole Year', 'Autumn', 'Rabi','Summer', 'Winter']
    # Strip whitespace from each element in the list
    season_names_stripped = [season.strip() for season in season]
    # Selectbox for choosing season names
    season_names = st.selectbox('Select Season', season_names_stripped)
    if not get_state().message_spoken['season']:
        #speak1("district for crop yield prediction.")
        get_state().message_spoken['season'] = True
    crop_by_district=['Groundnut', 'Jowar', 'Jute', 'Maize', 'Moong(Green Gram)', 'Niger seed', 'Other Kharif pulses', 'Rice', 'Sesamum', 'Small millets', 'Soyabean', 'Sunflower', 'Barley', 'Gram', 'Linseed', 'Other  Rabi pulses']
    crop_names=st.selectbox('select crop',crop_by_district)

    area = st.number_input('Area', min_value=1, max_value=8580100)
    temperature = st.number_input('Temperature', min_value=2.43, max_value=26.0)
    wind_speed = st.number_input('Wind Speed', min_value=0.27, max_value=3.49)
    precipitation = st.number_input('Precipitation', min_value=1009, max_value=1023)
    humidity = st.number_input('Humidity', min_value=37, max_value=97)
    soil_types = ['clay', 'sandy', 'peaty', 'chalky', 'silt', 'silty', 'loamy']
    soil_type = st.selectbox('Soil Type', soil_types)




# Button to trigger prediction
if st.button('Predict'):
    # Get input values
    
    
    features = np.array([[state_names, district_names, season_names, crop_names, area, temperature, wind_speed, precipitation, humidity, soil_type]], dtype=object)
    # Predict crop yield
    prediction = predict_production(state_names, district_names, season_names, crop_names, area, temperature, wind_speed, precipitation, humidity, soil_type)
    st.write(prediction[0])
    # Speak the prediction
    #speak1("click below paly to listen")
        
        #tts(f"Predicted crop yield Production is {prediction[0]}")
    speak1("Predicted Production is " )
        
