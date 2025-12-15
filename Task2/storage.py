import json
from datetime import datetime, timezone

FILE = "submissions.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save entries in "submissions":
# Timestamps saved as Timezone Aware UTC DateTime to avoid depreciation issues:
"""
def save_entry(entry: dict):
    data = load_data()
    entry["timestamp"] = datetime.now(timezone.utc).isoformat()

    data.append(entry)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)
"""
def save_entry(rating, review, ai_response):
    data = load_data()
    data.append({
        "rating": rating,
        "review": review,
        "ai_response": ai_response
    })
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


