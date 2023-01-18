import requests
import json

response = requests.get(
    'https://desktopchat.onrender.com/test-room/tpg', 
)

result = json.loads(response.content)
for i in result['messages']:
    print(i['message'])