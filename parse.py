from bs4 import BeautifulSoup
import requests

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx/5xx errors
        
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.prettify()  # Return prettified HTML
    
    except requests.RequestException as e:
        return f"Error fetching the URL: {e}"
    

def parse_info(html, attributes):
    attributes = [attribute.strip() for attribute in attributes if attribute.strip()]
    return attributes
