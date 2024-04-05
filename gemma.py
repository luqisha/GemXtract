import requests

API_URL = 'https://api-inference.huggingface.co/models/google/gemma-2b-it'
API_TOKEN = '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'

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	'inputs': 'What is your name?',
})

print(output[0]['generated_text'])