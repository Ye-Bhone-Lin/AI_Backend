import requests

response_research = requests.post("http://localhost:8000/codetest/invoke", json={"input":{"question": """done

"""}})
print(response_research.json()['output']['content'])