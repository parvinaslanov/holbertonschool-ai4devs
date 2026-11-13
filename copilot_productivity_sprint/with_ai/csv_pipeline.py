import csv
import json
from typing import List, Dict

def process_csv_to_json(input_filepath: str, output_filepath: str) -> List[Dict]:
    cleaned_records = []
    
    with open(input_filepath, mode="r", encoding="utf-8", newline="") as infile:
        reader = csv.DictReader(infile)
        for row_num, row in enumerate(reader, start=2):
            if not row or any(value is None or value.strip() == "" for value in row.values()):
                continue
            
            cleaned_row = {k.strip(): v.strip() for k, v in row.items()}
            cleaned_records.append(cleaned_row)
            
    with open(output_filepath, mode="w", encoding="utf-8") as outfile:
        json.dump(cleaned_records, outfile, indent=4)
        
    return cleaned_records
