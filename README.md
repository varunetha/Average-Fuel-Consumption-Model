# Average-Fuel-Consumption-Model
The Fuel Consumption Prediction App is an interactive web application built using Python and Streamlit that predicts the fuel consumption (in L/100km) of a vehicle based on its specifications. The app uses a trained machine learning model to provide accurate fuel efficiency predictions for various vehicles.


🚗 Fuel Consumption Prediction App
About the Project

The Fuel Consumption Prediction App is an interactive web application that predicts a vehicle’s fuel consumption in L/100km using machine learning. The app allows users to input various parameters such as vehicle class, engine size, number of cylinders, transmission type, CO2 rating, and fuel type, and provides an instant prediction based on a trained model.

This project combines data preprocessing, machine learning, and web app development to create a real-world tool for estimating fuel efficiency.

Key Features

Interactive Prediction Form: Users can input vehicle specifications through intuitive dropdowns and numeric inputs.

Real-Time Results: Fuel consumption is predicted and displayed instantly on the app.

Custom Styling: Modern, 3D-style input cards with hover effects for a realistic, visually appealing dashboard.

Background & Icons: Dynamic background image with vehicle and fuel icons for better UX.

Responsive Layout: Works on various screen sizes and devices.

How the Code Works

Model & Scaler Loading:

loaded_model = pk.load(open("train.sav", "rb"))
scaled_data = pk.load(open("scale.sav", "rb"))


The app loads a pre-trained machine learning model and a data scaler to normalize inputs.

Input Conversion:
The app converts user inputs into a numeric format suitable for the ML model.

Categorical variables (vehicle type, transmission, fuel type) are encoded.

Fuel type is one-hot encoded.

Numeric inputs (engine size, cylinders, CO2 rating) are scaled.

Prediction:

arr = scaled_data.transform(user_input_array)
prediction = loaded_model.predict(arr)


The app uses the trained model to predict fuel consumption.

Output Display:
The predicted fuel consumption is shown in a stylish result card on the webpage with dynamic formatting.

Libraries Used

Streamlit: For building the interactive web interface.

NumPy & Pandas: For data handling and preprocessing.

Scikit-learn: For loading the trained machine learning model and scaling data.

Pickle: To save and load the trained model and scaler.

Base64: To embed background images from local files.

HTML & CSS: For styling, hover effects, icons, and 3D card effects.

Sample Input & Output

Input:

Vehicle class: SUV: Small

Engine size: 4

Cylinders: 6

Transmission: AV

CO2 Rating: 7

Fuel Type: D

Output:

Fuel Consumption: 9.45 L/100km


The prediction is dynamically displayed in a visually appealing result panel.

How to Run the App

Clone the repository:

git clone https://github.com/your-username/fuel-consumption-app.git


Navigate to the project folder:

cd fuel-consumption-app


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

Future Improvements

Integrate vehicle images beside dropdowns for a more interactive experience.

Add more ML models for higher accuracy.

Deploy on Streamlit Cloud for public accessibility.

Include graphs and visualizations to show predicted fuel efficiency trends.
