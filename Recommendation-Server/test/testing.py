import requests

data = {
    'flag' : False,
    'soil' : 1,
    'season' : 1,
    'ph' : 6.5,
    'N' : 0,
    'P' : 0,
    'K' : 0,
    
    #'Temperature' : None,
    #'Humidity' : None,
    'Temperature' : 32,
    'Humidity' : 70,
    
    'Rainfall' : 100,
    'State' : 'Gujarat',
    'Area' : 'Ahmedabad',
    'Month' : 'July',
    
    'Latitude' : 23.4643,
    'Longitude' : 73.2988
}

resp = requests.post('http://localhost:5000/recommend', json=data)

print(resp.text)

# crop info
resp = requests.post('http://localhost:5000/crop_details', json={'about_crop' : 'Rice'})

print(resp.text)