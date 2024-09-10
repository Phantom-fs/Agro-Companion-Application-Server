import requests

resp = requests.post('http://localhost:5000/predict', files={'file': open('alluvial.jpeg', 'rb')})

print(resp.text)