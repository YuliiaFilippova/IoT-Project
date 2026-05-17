import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

SCREENSHOT_DIR = os.path.join(
    BASE_DIR,
    "../data/raw_events/screenshots"
)

CSV_DIR = os.path.join(
    BASE_DIR,
    "../data/telemetry/csv"
)

JSON_DIR = os.path.join(
    BASE_DIR,
    "../data/telemetry/json"
)

SEMANTIC_JSON_DIR = os.path.join(
    BASE_DIR,
    "../data/semantic_analysis/json"
)

PROCESSED_DIR = os.path.join(
    BASE_DIR,
    "../data/raw_events/processed"
)

os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(CSV_DIR, exist_ok=True)
os.makedirs(JSON_DIR, exist_ok=True)
os.makedirs(SEMANTIC_JSON_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)
