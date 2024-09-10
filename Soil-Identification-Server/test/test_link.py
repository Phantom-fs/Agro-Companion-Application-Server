import requests

resp = requests.post('.../predict', files={'file': open('alluvial.jpeg', 'rb')})

print(resp.text)