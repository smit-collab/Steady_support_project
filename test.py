import csv
import json

#function below takes two params
def convert_csv_to_json(csv_file, json_file):
    data = []

    #sample encodings
    encodings_to_try = ['utf-8', 'latin-1', 'cp1252']
    for encoding in encodings_to_try:
        try:
            with open(csv_file, 'r', encoding=encoding) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    inputs = [item.strip() for item in row["Questions"].split('|')]
                    outputs = [item.strip() for item in row["Answers"].split('|')]
                    data.append({"inputs": inputs, "outputs": outputs})
            break
        except UnicodeDecodeError:
            continue 
    with open(json_file, 'w', encoding='utf-8') as json_output:
        json.dump(data, json_output, indent=2)

csv_file = 'mh_questions.csv'
json_file = 'output.json'
convert_csv_to_json(csv_file, json_file)
