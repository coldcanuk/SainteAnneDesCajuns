import requests
from bs4 import BeautifulSoup
import hashlib
import os
import json

def generate_hash(url):
    return hashlib.md5(url.encode()).hexdigest()

def extract_and_save_if_new(url, base_path='urlOffers/'):
    hash_name = generate_hash(url)
    file_path = os.path.join(base_path, hash_name + '.url')

    response_data = {
        "URL": url,
        "HASH": hash_name,
        "DATE_DOWNLOADED": None
    }

    if os.path.exists(file_path):
        response_data["DATE_DOWNLOADED"] = os.path.getmtime(file_path)
        return json.dumps(response_data)
    else:
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            text = ' '.join(paragraph.get_text() for paragraph in paragraphs)

            os.makedirs(base_path, exist_ok=True)
            os.makedirs('urlPREPARSED/', exist_ok=True)
            os.makedirs('urlPOSTPARSED/', exist_ok=True)

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(url)
            with open('urlPREPARSED/' + hash_name + '.preparsed', 'w', encoding='utf-8') as file:
                file.write(text)

            response_data["DATE_DOWNLOADED"] = os.path.getmtime(file_path)
            return json.dumps(response_data)
        except requests.RequestException as e:
            print(f"Error occurred: {e}")
            return None
