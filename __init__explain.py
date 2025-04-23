import requests

response_research = requests.post(
    "http://localhost:8000/steps/invoke",
    json={"input":{
        "input": """
 {
      "step_number": 2,
      "title": "Python Programming for AI",
      "description": "Learn Python programming language and its applications in AI",
      "resource_url": "https://www.python.org/about/gettingstarted/coding/",
      "estimated_time_minutes": 180
    }
"""
    }}
)

print(response_research.json()['output']['content'])
