import requests
import time

CANDIDATE_ID = "41420640-06e3-4e73-b989-5891f4db200d"

BASE_URL_POLYANET = "https://challenge.crossmint.io/api/polyanets"
BASE_URL_SOLOON = "https://challenge.crossmint.io/api/soloons"
BASE_URL_COMETH = "https://challenge.crossmint.io/api/comeths"

GRID_SIZE = 11 

# --- API DELETE functions ---

def delete_polyanet(row, column):
    _delete(BASE_URL_POLYANET, {
        "candidateId": CANDIDATE_ID,
        "row": row,
        "column": column
    }, f"polyanet ({row},{column})")

def delete_soloon(row, column):
    _delete(BASE_URL_SOLOON, {
        "candidateId": CANDIDATE_ID,
        "row": row,
        "column": column
    }, f"soloon ({row},{column})")

def delete_cometh(row, column):
    _delete(BASE_URL_COMETH, {
        "candidateId": CANDIDATE_ID,
        "row": row,
        "column": column
    }, f"cometh ({row},{column})")

# --- Helper DELETE with retry ---

def _delete(url, payload, label):
    for attempt in range(3):
        response = requests.delete(url, json=payload)
        if response.status_code == 200:
            print(f" Deleted {label}")
            return
        else:
            print(f"Failed to delete ({response.status_code}): {label} - {response.text}")
            time.sleep(2)

# --- Main ---

def main():
    print("Resetting all elements in grid...")
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            delete_polyanet(row, column)
            delete_soloon(row, column)
            delete_cometh(row, column)
            time.sleep(1.0)  # avoid 429 errors

if __name__ == "__main__":
    main()
