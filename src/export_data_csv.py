import os
import json
import pandas as pd

from utils.paths import FINAL_EVENT_DIR


rows = []

for filename in os.listdir(FINAL_EVENT_DIR):

    if not filename.endswith(".json"):
        continue

    json_path = os.path.join(
        FINAL_EVENT_DIR,
        filename
    )

    with open(json_path, "r") as f:
        event = json.load(f)

    for species in event.get("species", []):

        rows.append({

            "event_id":
                event.get("event_id"),

            "species":
                species.get("name"),

            "count":
                species.get("count"),

            "dominant_species":
                event.get("dominant_species"),

            "behavior":
                event.get("behavior"),

            "interaction":
                event.get("interaction"),

            "activity_level":
                event.get("activity_level"),

            "event":
                event.get("event"),

            "daytime":
                event.get("daytime"),

            "weather":
                event.get("weather")
        })


df = pd.DataFrame(rows)

output_path = "species_observations.csv"

df.to_csv(
    output_path,
    index=False
)

print(df.head())

print(f"\nSaved: {output_path}")