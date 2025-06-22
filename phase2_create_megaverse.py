import requests
import time

CANDIDATE_ID = "41420640-06e3-4e73-b989-5891f4db200d"

BASE_URL_POLYANET = "https://challenge.crossmint.io/api/polyanets"
BASE_URL_SOLOON = "https://challenge.crossmint.io/api/soloons"
BASE_URL_COMETH = "https://challenge.crossmint.io/api/comeths"
BASE_URL_GOAL = f"https://challenge.crossmint.io/api/map/{CANDIDATE_ID}/goal"
MAX_RETRIES = 3

# --- API functions ---

def create_polyanet(row, column):
    _post(BASE_URL_POLYANET, {
        "candidateId": CANDIDATE_ID,
        "row": row,
        "column": column
    }, f"polyanet ({row},{column})")

def create_soloon(row, column, color):
    _post(BASE_URL_SOLOON, {
        "candidateId": CANDIDATE_ID,
        "row": row,
        "column": column,
        "color": color
    }, f"soloon ({color}) ({row},{column})")

def create_cometh(row, column, direction):
    _post(BASE_URL_COMETH, {
        "candidateId": CANDIDATE_ID,
        "row": row,
        "column": column,
        "direction": direction
    }, f"cometh ({direction}) ({row},{column})")

# --- Helper POST with retry ---

def _post(url, payload, label):
    for attempt in range(MAX_RETRIES):
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"Created {label}")
            return
        else:
            print(f"Failed ({response.status_code}): {label} - {response.text}")
            time.sleep(2)

# --- Fetch goal map ---

def fetch_goal_map():
    response = requests.get(BASE_URL_GOAL)
    if response.status_code == 200:
        print("Fetched goal map")
        return response.json()["goal"]
    else:
        print(f" Failed to fetch goal map: {response.status_code}")
        return []

# --- Extract functions ---

def extract_color(cell_text):
    return cell_text.split("_")[0].lower()

def extract_direction(cell_text):
    return cell_text.split("_")[0].lower()


def main():
    goal_map = fetch_goal_map()

    for row_index, row in enumerate(goal_map):
        for column_index, cell in enumerate(row):
            if "POLYANET" in cell:
                create_polyanet(row_index, column_index)
            elif "SOLOON" in cell:
                color = extract_color(cell)
                create_soloon(row_index, column_index, color)
            elif "COMETH" in cell:
                direction = extract_direction(cell)
                create_cometh(row_index, column_index, direction)

            time.sleep(1.0)  # avoid 429 errors

if __name__ == "__main__":
    main()
