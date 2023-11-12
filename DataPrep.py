import json

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def clean_and_format_data(text):
    # Implement cleaning and formatting logic here
    return text.strip()

def save_data(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)