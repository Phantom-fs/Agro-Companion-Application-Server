from flask import jsonify
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

import pickle

# Example data
# fuzzy logic implementation of "crop_recommendation_system" will be made available upon request

# --------------------------------------------------------------------------------

# CROP LABELS
# Define the ranges for the output crops
crop = ctrl.Consequent(np.arange(0, 24, 1), 'crop')

# Define membership functions for the crops
crop['Rice'] = fuzz.trimf(crop.universe, [0, 0, 1])
crop['Wheat'] = fuzz.trimf(crop.universe, [1, 1, 2])
crop['Maize (Corn)'] = fuzz.trimf(crop.universe, [2, 2, 3])
crop['Cotton'] = fuzz.trimf(crop.universe, [3, 3, 4])
crop['Millets'] = fuzz.trimf(crop.universe, [4, 4, 5])
crop['Sugarcane'] = fuzz.trimf(crop.universe, [5, 5, 6])
crop['Rubber'] = fuzz.trimf(crop.universe, [6, 6, 7])
crop['Jute'] = fuzz.trimf(crop.universe, [7, 7, 8])
crop['Oilseeds'] = fuzz.trimf(crop.universe, [8, 8, 9])
crop['Pulses'] = fuzz.trimf(crop.universe, [9, 9, 10])
crop['Pearl Millet (Bajra)'] = fuzz.trimf(crop.universe, [10, 10, 11])
crop['Lentil'] = fuzz.trimf(crop.universe, [11, 11, 12])
crop['Groundnut'] = fuzz.trimf(crop.universe, [12, 12, 13])
crop['Cocoa'] = fuzz.trimf(crop.universe, [13, 13, 14])
crop['Tea'] = fuzz.trimf(crop.universe, [14, 14, 15])
crop['Coffee'] = fuzz.trimf(crop.universe, [15, 15, 16])
crop['Flaxseed'] = fuzz.trimf(crop.universe, [16, 16, 17])
crop['Coconut'] = fuzz.trimf(crop.universe, [17, 17, 18])
crop['Oil palm'] = fuzz.trimf(crop.universe, [18, 18, 19])
crop['Clove'] = fuzz.trimf(crop.universe, [19, 19, 20])
crop['Black pepper'] = fuzz.trimf(crop.universe, [20, 20, 21])
crop['Cardamom'] = fuzz.trimf(crop.universe, [21, 21, 22])
crop['Turmeric'] = fuzz.trimf(crop.universe, [22, 22, 23])

# CROP LABELS
crops = ['Rice', 'Wheat', 'Maize (Corn)', 'Cotton', 'Millets', 'Sugarcane', 'Rubber', 'Jute', 'Oilseeds', 'Pulses',
            'Pearl Millet (Bajra)', 'Lentil', 'Groundnut', 'Cocoa', 'Tea', 'Coffee', 'Flaxseed', 'Coconut', 'Oil palm',
            'Clove', 'Black pepper', 'Cardamom', 'Turmeric']

def recommendation_system(soil_input, season_input, ph_input, N_input, P_input, K_input, Temperature_input, Humidity_input, Rainfall_input, flag):
    # Select the model based on the flag
    if flag == "True":
        with open('files_app/crop_recommendation_system_with_NPK.pkl', 'rb') as file:
            crop_recommendation_system = pickle.load(file)
    elif flag == "False":
        with open('files_app/crop_recommendation_system_without_NPK.pkl', 'rb') as file:
            crop_recommendation_system = pickle.load(file)
        # Update the N, P, K values to 0, safety check
        N_input = 0
        P_input = 0
        K_input = 0
    else:
        return jsonify({'error': 'flag should be either True or False'})
      
    # --------------------------------------------------------------------------------
    # CROP LABELS   
    try:
        crop_recommendation_system.input['soil'] = soil_input
        crop_recommendation_system.input['season'] = season_input
        crop_recommendation_system.input['ph'] = ph_input
        crop_recommendation_system.input['N'] = N_input
        crop_recommendation_system.input['P'] = P_input
        crop_recommendation_system.input['K'] = K_input
        crop_recommendation_system.input['Temperature'] = Temperature_input
        crop_recommendation_system.input['Humidity'] = Humidity_input
        crop_recommendation_system.input['Rainfall'] = Rainfall_input

        crop_recommendation_system.compute()
                
        # Multiple crops
        crop_output = crop_recommendation_system.output['crop']

        # Defuzzify the output to get membership values
        crop_values = {key: fuzz.interp_membership(crop.universe, crop[key].mf, crop_output) for key in crop.terms}

        crop_scores = {key: value * 100 for key, value in crop_values.items()}

        # Sort crops by their scores in descending order
        crop_scores_percent = sorted(crop_scores.items(), key=lambda x: x[1], reverse=True)
        
        # remove the crops with 0% score
        recommended_crop_multiple_percent = [x for x in crop_scores_percent if x[1] > 0]
        
        return recommended_crop_multiple_percent
    
    except:
        return None