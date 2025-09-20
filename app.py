import numpy as np
import pickle as pk
import streamlit as st
import base64

# Load model and scaler
loaded_model = pk.load(open("train.sav", "rb"))
scaled_data = pk.load(open("scale.sav", "rb"))

# Helper function to convert local image to base64
@st.cache_data
def get_img_as_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Convert local image to base64
img_base64 = get_img_as_base64("photo.jpg")

# Set the background image in CSS
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/jpg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
</style>
""", unsafe_allow_html=True)

# CSS for inputs and result boxes
st.markdown("""
<style>
.stSelectbox, .stNumberInput {
    border-radius: 12px;
    padding: 10px;
    background: rgba(0,0,0,0.5);
    color: white;
    font-weight: bold;
    box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
    transition: transform 0.2s, box-shadow 0.2s;
}
.stSelectbox:hover, .stNumberInput:hover {
    transform: translateY(-5px);
    box-shadow: 8px 8px 20px rgba(0,0,0,0.7);
}
h1 {
    text-align: center;
    color: #ffffff;
    text-shadow: 2px 2px 10px #000000;
}
.result-box {
    background: rgba(0,0,0,0.5);
    padding: 20px;
    border-radius: 15px;
    color: #fff;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    box-shadow: 5px 5px 15px rgba(0,0,0,0.7);
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Input converter function
def input_converter(inp):
    vcl = ['Two-seater','Minicompact','Compact','Subcompact','Mid-size','Full-size',
           'SUV: Small','SUV: Standard','Minivan','Station wagon: Small',
           'Station wagon: Mid-size','Pickup truck: Small','Special purpose vehicle',
           'Pickup truck: Standard']
    trans = ['AV','AM','M','AS','A']
    fuel = ["D","E","X","Z"]

    lst = [vcl.index(inp[0]), inp[1], inp[2], trans.index(inp[3]), inp[4]]
    fuel_one_hot = [1 if i == fuel.index(inp[5]) else 0 for i in range(len(fuel))]
    lst.extend(fuel_one_hot)

    arr = np.array(lst).reshape(1, -1)
    arr = scaled_data.transform(arr)
    prediction = loaded_model.predict(arr)
    return round(prediction[0], 2)

# Main app
st.markdown("<h1>🚗 Fuel Consumption Predictor 🚀</h1>", unsafe_allow_html=True)

vehicle = ['Two-seater','Minicompact','Compact','Subcompact','Mid-size','Full-size','SUV: Small',
           'SUV: Standard','Minivan','Station wagon: Small','Station wagon: Mid-size','Pickup truck: Small',
           'Special purpose vehicle','Pickup truck: Standard']
transmission = ['AV','AM','M','AS','A']
fuel_type = ["D","E","X","Z"]

Vehicle_class = st.selectbox("🚘 Vehicle class", options=vehicle)
Engine_size = st.selectbox("⚙️ Engine Size (1-7)", options=list(range(1,8)))
Cylinders = st.number_input(" Cylinders (1-16)", min_value=1, max_value=16)
Transmission = st.selectbox("🔧 Transmission", options=transmission)
Co2_Rating = st.number_input("🌿 CO2 Rating (1-10)", min_value=1, max_value=10)
Fuel_type_input = st.selectbox("⛽ Fuel type", options=fuel_type)

if st.button("Predict 🔍"):
    result = input_converter([Vehicle_class, Engine_size, Cylinders, Transmission, Co2_Rating, Fuel_type_input])
    st.markdown(f"<div class='result-box'>Fuel Consumption: {result} L/100km</div>", unsafe_allow_html=True)
