import requests
import streamlit as st

API_URL = 'https://api-inference.huggingface.co/models/google/gemma-7b-it'
API_TOKEN = st.secrets['HF_API_TOKEN'] # Or you can replace this with your 🤗 token


headers = {"Authorization": f"Bearer {API_TOKEN}"}


def ask_gemma(html, attributes):
	prompt = "Task: Given the HTML body and a list of Attributes below, create a JSON object. The JSON keys should be the attributes, and their values should be lists of the content associated with each attribute found in the HTML. \n\nOutput: Only the resulting JSON object. Nothing else. \n\n"
	
	payload = {
		"inputs": prompt + "Attributes: " + str(attributes) + "\n\nHTML body: " + html
	}

	response = requests.post(API_URL, headers=headers, json=payload).json()
	
	return response
