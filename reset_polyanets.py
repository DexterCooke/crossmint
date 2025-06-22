import requests
import time


CANDIDATE_ID = "41420640-06e3-4e73-b989-5891f4db200d"

BASE_URL = "https://challenge.crossmint.io/api/polyanets"
GRID_SIZE = 11  # Full grid

class PolyanetAPI:
    def __init__(self, candidate_id):
        self.candidate_id = candidate_id

    def delete_polyanet(self, row, column):
        for attempt in range(3):
            response = requests.delete(
                BASE_URL,
                json={
                    "candidateId": self.candidate_id,
                    "row": row,
                    "column": column
                }
            )
            if response.status_code == 200:
                print(f"Deleted polyanet at ({row}, {column})")
                return
            else:
                print(f"Failed to delete at ({row}, {column}): {response.status_code} - {response.text}")
                time.sleep(2)

def main():
    api = PolyanetAPI(CANDIDATE_ID)


    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            api.delete_polyanet(row, column)
            time.sleep(1.0)  # be kind to API

if __name__ == "__main__":
    main()
