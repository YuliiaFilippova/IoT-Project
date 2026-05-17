import os
import shutil

from datetime import datetime

from semantic.qwen_vlm import analyze_frames

from semantic.reasoning_llm import build_semantic_state

from events.detect_events import detect_event

from storage.save_json import save_json
from utils.paths import SEMANTIC_JSON_DIR

from utils.paths import (
    SCREENSHOT_DIR,
    PROCESSED_DIR
)


previous_state = None


def run_semantic_pipeline():

    global previous_state

    for filename in os.listdir(SCREENSHOT_DIR):

        if not filename.endswith(".jpg"):
            continue

        image_path = os.path.join(
            SCREENSHOT_DIR,
            filename
        )

        try:

            print(f"Analyzing: {filename}")

            # VLM
            vlm_output = analyze_frames(
                [image_path]
            )

            print(vlm_output)

            # LLM STRUCTURING
            semantic_state = build_semantic_state(
                vlm_output
            )

            # METADATA
            semantic_state["timestamp"] = str(
                datetime.now()
            )

            semantic_state["source_image"] = filename

            # EVENTS
            semantic_state["event"] = detect_event(
                previous_state,
                semantic_state
            )

            previous_state = semantic_state

            # SAVE
            save_json(semantic_state, SEMANTIC_JSON_DIR)

            # MOVE PROCESSED IMAGE
            shutil.move(
                image_path,
                os.path.join(
                    PROCESSED_DIR,
                    filename
                )
            )

            print(f"Processed: {filename}")

        except Exception as e:

            print(f"Failed processing {filename}")

            print(e)