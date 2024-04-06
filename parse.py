import requests
from bs4 import BeautifulSoup
from agents import ask_gemma


def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx/5xx errors
        
        soup = BeautifulSoup(response.text, 'html.parser').find('body')
        return soup.prettify()
    
    except requests.RequestException as e:
        return f"Error fetching the URL 🤕 \n\n{e}"
    

def parse_info(html, tags):
    attributes = [tag.strip() for tag in tags if tag.strip()]
    agent_response = ask_gemma(html, attributes)

    return agent_response if agent_response else 'No response from the agent 🤖'


def sanitize(text):
    json_part = None
    marker = '{'
    start_index = text.rfind(marker)

    if start_index != -1:
        # Extract the JSON object portion starting from the marker
        json_part = text[start_index : ].strip().replace('`', '')
        print(json_part)
        return json_part

    else:
        print('Marker not found in the string.')
        return 'No gem found 🤕'