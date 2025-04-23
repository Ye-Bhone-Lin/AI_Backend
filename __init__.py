import requests

response_research = requests.post("http://localhost:8000/roadmap/invoke", json={"input":{"input": "I want to learn AI Engineer now I am beginner level."}})
print(response_research.json()['output']['content'])

"""
Here's a suggested learning path for AI engineering, tailored to a beginner level. I'll provide a JSON output with a structured plan.

```json
{
  "id": 1,
  "title": "AI Engineer Learning Path",
  "description": "A step-by-step guide to becoming an AI Engineer",
  "language": "English",
  "difficulty_level": "Beginner",
  "ai_generated": true,
  "steps": [
    {
      "step_number": 1,
      "title": "Introduction to AI and Machine Learning",
      "description": "Learn the basics of AI, ML, and DL. Understand the types of AI, ML, and DL.",   
      "resource_url": "https://www.coursera.org/specializations/machine-learning",
      "estimated_time_minutes": 120
    },
    {
      "step_number": 2,
      "title": "Python Programming",
      "description": "Learn Python basics, including data structures, file operations, and object-oriented programming.",
      "resource_url": "https://www.python.org/about/gettingstarted/coding/",
      "estimated_time_minutes": 180
    },
    {
      "step_number": 3,
      "title": "Frontend Framework - Not Required",
      "description": "As an AI Engineer, you won't need frontend development skills. Focus on backend and data science skills.",
      "resource_url": "",
      "estimated_time_minutes": 0
    },
    {
      "step_number": 4,
      "title": "Mathematics and Statistics for AI",
      "description": "Learn linear algebra, calculus, probability, and statistics. Understand how to apply these concepts to AI and ML.",
      "resource_url": "https://www.khanacademy.org/math",
      "estimated_time_minutes": 240
    },
    {
      "step_number": 5,
      "title": "AI and ML Frameworks",
      "description": "Learn popular AI and ML frameworks like TensorFlow, PyTorch, or Scikit-learn. Practice building projects using these frameworks.",
      "resource_url": "https://www.tensorflow.org/tutorials",
      "estimated_time_minutes": 300
    }
  ]
}
```

This learning path focuses on the essential skills required to become an AI Engineer. You'll start with an introduction to AI and ML, followed by Python programming, mathematics, and statistics. Finally, you'll learn AI and ML frameworks and practice building projects.

Feel free to adjust the estimated time and resources according to your pace and preferences. Good luck on your AI Engineer journey!
"""