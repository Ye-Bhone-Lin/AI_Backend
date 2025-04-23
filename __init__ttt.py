import requests

response = requests.post("http://localhost:8000/chat/", json={"prompt":"ဘယ်လိုလေ့လာလို့ရနိုင်မလဲ"})

result = response.json()

print(result['response']['response'])