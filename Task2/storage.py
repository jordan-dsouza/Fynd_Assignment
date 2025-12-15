import json
from datetime import datetime, timezone
from pathlib import Path

# Absolute path relative to this file
BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "submissions.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save entries in "submissions":
def save_entry(rating, review, ai_response):
    data = load_data()
    data.append({
        "rating": rating,
        "review": review,
        "ai_response": ai_response
    })
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
