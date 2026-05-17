import cv2
import time

from datetime import datetime

from collector.capture_stream import open_stream
from collector.trigger_logic import TriggerAnalyzer

from detection.yolo_detect import detect_animals

from metadata.detect_daytime import detect_daytime
from metadata.extract_weather import extract_temperature

from storage.save_screenshot import save_screenshot
from storage.save_json import save_json
from storage.save_csv import save_csv

from utils.paths import JSON_DIR


YOUTUBE_URL = "https://www.youtube.com/watch?v=4kRzwJXaeIM"

cap = open_stream(YOUTUBE_URL)

# IMPORTANT
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

trigger = TriggerAnalyzer()

frame_counter = 0

while True:

    ret, frame = cap.read()
    frame = cv2.resize(frame, (960, 540))
    #frame = cv2.resize(frame, (640, 360))

    if not ret:

        print("Stream connection lost")

        cap.release()

        time.sleep(5)

        print("Reconnecting stream...")

        cap = open_stream(YOUTUBE_URL)

        continue

    frame_counter += 1

    # ALWAYS show smooth livestream
    display_frame = frame.copy()

    trigger_text = "MONITORING"

    animal_count = 0

    # ONLY process every 10th frame
    if frame_counter % 10 == 0:

        yolo_output = detect_animals(frame)

        animal_count = yolo_output["animal_count"]

        display_frame = yolo_output["annotated_frame"]

        print(f"Animals: {animal_count}")

        if trigger.should_trigger(animal_count):

            trigger_text = "TRIGGERED"

            print("Event Triggered")

            screenshot_filename = save_screenshot(frame)

            telemetry = {

                "timestamp": str(datetime.now()),

                "animal_count": animal_count,

                "detections": yolo_output["detections"],

                "daytime": detect_daytime(frame),

                "screenshot": screenshot_filename
            }

            save_json(
                telemetry,
                JSON_DIR
            )

            save_csv({

                "timestamp": telemetry["timestamp"],

                "animal_count": telemetry["animal_count"],

                "daytime": telemetry["daytime"]
            })

    # OVERLAYS
    cv2.putText(
        display_frame,
        f"Animals: {animal_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        display_frame,
        trigger_text,
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    # SMOOTH DISPLAY
    cv2.imshow(
        "Wildlife Analytics Live",
        display_frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()