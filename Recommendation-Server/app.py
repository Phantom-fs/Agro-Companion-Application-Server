from flask import Flask, request, jsonify
from flask_cors import CORS

import requests

from files_app.rainfall import rainfall_info
from files_app.recommendation import recommendation_system
from files_app.crop_info import crop_info_details

app = Flask(__name__)

# enable CORS
CORS(app) # UPDATE IT TO WEBSITE URL

# Default route
@app.route('/')
def home():
    return "<p>Soil Classification and Crop Recommendation</p>"
        
@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == 'POST':
        data = request.json
        
        flag = data.get('flag')
        
        soil = data.get('soil')
        season = data.get('season')
        ph = data.get('ph')
        
        N = data.get('N')
        P = data.get('P')
        K = data.get('K')
        
        Temperature = data.get('Temperature')
        Humidity = data.get('Humidity')
        
        Rainfall = data.get('Rainfall')
        
        # data for rainfall 
        state = data.get('State')
        area = data.get('Area')
        month = data.get('Month')
        
        lat = data.get('Latitude')
        lon = data.get('Longitude')
        
        try:
            if Temperature == "NA" or Humidity == "NA":
                # API_key = 'ENTER THE API KEY FROM OPENWEATHER API'
                web = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
                
                # get the weather data
                weather_data = requests.get(web)
                weather_data = weather_data.json()
                
                # get the temperature
                if Temperature == "NA":
                    Temperature = weather_data['main']['temp']
                    # convert temperature from kelvin to celsius
                    Temperature = Temperature - 273.15
                
                # get the humidity
                if Humidity == "NA":
                    Humidity = weather_data['main']['humidity']      
        except:
            return jsonify({'error': 'error during weather data fetching'})
        
        try:
            if Rainfall == "NA" and (month != "NA" and state != "NA" and area != "NA"):
                # get the rainfall data
                Rainfall = rainfall_info(state, area, month)
        except:
            return jsonify({'error': 'data not found for the given state and area. Please try again with different inputs'})
        
        try:
            # get the crop recommendation
            crop_recommendation = recommendation_system(soil, season, ph, N, P, K, Temperature, Humidity, Rainfall, flag)
            
            return jsonify({'crop_recommendation': crop_recommendation})
        except:
            return jsonify({'error': 'No crop recommendation found, please try again with different inputs'})
     
@app.route('/crop_details', methods=['POST'])
def crop_details():
    if request.method == 'POST':
        data = request.json
        
        crop = data.get('about_crop')
        
        try:
            # get the crop details
            crop_info = crop_info_details(crop)
            
            # change to string
            crop_info = str(crop_info)
            
            return jsonify({'crop_info': crop_info})
        except:
            return jsonify({'error': 'No crop details found, please try again with different inputs'})