import csv
import requests

csv_file = "Task 2 - Intern.csv"

with open(csv_file, newline='', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)

    for row in reader:
        # safely extract URL regardless of header issues
        url = list(row.values())[0].strip()

        try:
            response = requests.head(url, timeout=5)

            # fallback if HEAD fails or is blocked
            if response.status_code >= 400:
                response = requests.get(url, timeout=5)

            print(f"({response.status_code}) {url}")

        except requests.exceptions.RequestException as e:
            print(f"({type(e).__name__}) {url}")