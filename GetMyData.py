import requests
from bs4 import BeautifulSoup

def extract_text_from_web(url):
    if not url:
        raise ValueError("No URL provided")

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join(paragraph.get_text() for paragraph in paragraphs)

        return text
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
        return None

def save_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)
