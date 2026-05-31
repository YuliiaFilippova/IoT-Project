import os
import shutil
#from datetime import datetime
from semantic.qwen_vlm import analyze_frames

from semantic.reasoning_llm import build_semantic_state

from events.detect_events import detect_event

from storage.save_json import save_json
#from utils.paths import SEMANTIC_JSON_DIR

from utils.paths import (
    RAW_EVENT_DIR,
    FINAL_EVENT_DIR,
    PROCESSED_DIR,
    SCREENSHOT_DIR
)

import json


previous_state = None


def run_semantic_pipeline():

    global previous_state

    for filename in os.listdir(RAW_EVENT_DIR):

        if not filename.endswith(".json"):
            continue

        json_path = os.path.join(
            RAW_EVENT_DIR,
            filename
        )

        try:
            with open(json_path, "r") as f:
                event_data = json.load(f)

            image_path = os.path.join(
                SCREENSHOT_DIR,
                event_data["screenshot"]
            )

            print(f"Analyzing: {image_path}")

            #print(f"Analyzing: {filename}")

            # VLM
            vlm_output = analyze_frames(
                [image_path]
            )

            print(vlm_output)

            # LLM STRUCTURING
            semantic_state = build_semantic_state(
                vlm_output
            )

            # MERGE RAW EVENT DATA + SEMANTICS
            final_event = {
                **event_data,
                **semantic_state
            }

            #final_event["observation"] = vlm_output

            # EVENT DETECTION
            final_event["event"] = detect_event(
                previous_state,
                final_event
            )

            previous_state = final_event

            final_event.pop("detections", None)
            final_event.pop("timestamp", None)
            final_event.pop("observation", None)
            #final_event.pop("screenshot", None)
            final_event.pop("animal_count", None)

            # SAVE FINAL RESULT
            save_json(
                final_event,
                FINAL_EVENT_DIR,
                final_event["event_id"]
            )

            # MOVE PROCESSED IMAGE
            shutil.move(
                image_path,
                os.path.join(
                    PROCESSED_DIR,
                    event_data["screenshot"]
                )
            )

            # REMOVE RAW EVENT JSON
            os.remove(json_path)

            print(f"Processed: {filename}")

        except Exception as e:

            print(f"Failed processing {filename}")

            print(e)