import requests

response_research = requests.post("http://localhost:8000/codetest/invoke", json={"input":{"question": """def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ''.join([char for char in s if char not in vowels])
    return result

# Test the function with an example
input_string = "hello world"
output_string = remove_vowels(input_string)
print(output_string)
"""}})
print(response_research.json())