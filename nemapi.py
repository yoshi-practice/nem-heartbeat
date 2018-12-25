import requests
import json

r = requests.get('http://23.228.67.85:7890/heartbeat').json()

print(r)
