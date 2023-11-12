from SaintPierredeSolesmes import extract_and_save_if_new
from DataPrep import read_text_file, clean_and_format_data, save_data
import json

url = "https://en.wikipedia.org/wiki/Expulsion_of_the_Acadians"

result_json = extract_and_save_if_new(url)
result = json.loads(result_json)

if result and result["HASH"]:
    hash_name = result["HASH"]
    raw_file = f'urlPREPARSED/{hash_name}.preparsed'
    formatted_file = f'urlPOSTPARSED/{hash_name}.postparsed'

    raw_text = read_text_file(raw_file)
    if raw_text:
        formatted_data = clean_and_format_data(raw_text)
        save_data(formatted_data, formatted_file)
    else:
        print("Error: No text found in the raw output file.")
else:
    print(f"Error or data already exists: {result}")