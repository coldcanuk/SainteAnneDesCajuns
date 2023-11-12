# LeCardinal.py - Orchestrates the flow between GetMyData.py and DataPrep.py

from GetMyData import extract_text_from_web, save_text_to_file
from DataPrep import read_text_file, clean_and_format_data, save_data

url = "https://en.wikipedia.org/wiki/Expulsion_of_the_Acadians"
raw_output_file = 'extracted_text.txt'
formatted_output_file = 'formatted_data.json'

extracted_text = extract_text_from_web(url)
if extracted_text:
    save_text_to_file(extracted_text, raw_output_file)

    raw_text = read_text_file(raw_output_file)
    if raw_text:
        formatted_data = clean_and_format_data(raw_text)
        save_data(formatted_data, formatted_output_file)
    else:
        print("Error: No text found in the raw output file.")
else:
    print("Error: No text extracted from the URL.")
