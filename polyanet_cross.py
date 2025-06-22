import requests
import time


CANDIDATE_ID = "41420640-06e3-4e73-b989-5891f4db200d"
BASE_URL = "https://challenge.crossmint.io/api/polyanets"
MIN_INDEX = 2
MAX_INDEX = 8
MAX_RETRIES = 3

class PolyanetAPI:
    def __init__(self, candidate_id):
        self.candidate_id = candidate_id

    def create_polyanet(self, row, column):
        for attempt in range(MAX_RETRIES):
            response = requests.post(
                BASE_URL,
                json={
                    "candidateId": self.candidate_id,
                    "row": row,
                    "column": column
                }
            )
            if response.status_code == 200:
                print(f"Created polyanet at ({row}, {column})")
                return
            else:
                print(f"Failed at ({row}, {column}): {response.status_code} - {response.text}")
                time.sleep(1)  # wait after failure and retry

def main():
    api = PolyanetAPI(CANDIDATE_ID)

    for row in range(2, 9): 
        for column in range(2, 9):
            if row == column or (row + column) == (MIN_INDEX + MAX_INDEX):
                api.create_polyanet(row, column)
                time.sleep(1.0)  # Slow enough to avoid 429 errors

if __name__ == "__main__":
    main()
