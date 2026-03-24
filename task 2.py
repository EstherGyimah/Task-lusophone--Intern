import csv
import requests

#csv file path
csv_file = "Task 2 - Intern.csv"

with open(csv_file, newline='', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    url_col = next(k for k in reader.fieldnames if 'url' in k.lower())

    for row in reader:
        url = row[url_col].strip()

        try:
            response = requests.get(url, timeout=5)
            print(f"({response.status_code}) {url}")
        except requests.exceptions.RequestException:
            print(f"(ERROR) {url}")