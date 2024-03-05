import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import streamlit as st
import time

# Set Streamlit app to wide mode
st.set_page_config(layout="wide")

# Define custom CSS for green text and radiant outline
custom_css = """
<style>
    .green-text {
        color: red;
        background: linear-gradient(45deg, #ffcc00, #00ccff);
        border: 6px solid transparent;
        border-image: linear-gradient(45deg, #ffcc00, #00ccff);
        border-image-slice: 1;
        padding: 10px;
        border-radius: 10px;
        font-size: 24px;
    }
</style>
"""

# Display the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Display the green text with radiant outline
st.markdown("<p class='green-text'><b>Welcome to the Crop Yield Prediction App!</p>", unsafe_allow_html=True)



selected=option_menu(
    menu_title=None,
    options=["Home ","English","తెలుగు"],
    icons=["house","alphabet-uppercase","/telugu.png"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if selected=="Home":
    
    background_css = f"""
<style>
body {{
    background-image: url('telugu.png');
    background-size: cover;
}}
</style>
"""

# Display the CSS using st.markdown
    st.markdown(background_css, unsafe_allow_html=True)

if selected=="English":
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
    pickled_model=pickle.load(open('dtr1.pkl','rb'))
    f=pickle.load(open('preprocessor1.pkl','rb'))



    def predict_production(state_names, district_names, season_names, crop_names, area, temperature, wind_speed, precipitation, humidity, soil_type):
        
        features = np.array([[state_names, district_names, season_names, crop_names, area, temperature, wind_speed,precipitation, humidity, soil_type]], dtype=object)
        print(features)
        # Transform the features using the preprocessor
        transformed_features = f.transform(features)

        # Make the prediction using the trained model
        predicted_production = pickled_model.predict(transformed_features).reshape(1, -1)

        return predicted_production[0]

    # Streamlit UI
    st.title('Crop Yield Prediction')

    def get_state():
        return st.session_state

    if 'message_spoken' not in get_state():
        get_state().message_spoken = {'intro': False,'state': False, 'district': False, 
                                    'season': False,'crop': False, 'area': False, 'temperature': False,
                                    'wind_speed': False, 'precipitation': False,
                                    'humidity': False, 'soil_type': False,'prediction':False}

    # Speak the message for introduction if it hasn't been spoken before
    if not get_state().message_spoken['intro']:
        #speak1("Please provide the following details for crop yield prediction.")
        g = gTTS( "Please provide the following details for crop yield prediction.",lang='en-uk', slow=False)
        g.save("eintro.mp3")
        playsound("eintro.mp3")
        os.remove('eintro.mp3')
        get_state().message_spoken['intro'] = True

if selected=="తెలుగు":
    pass
