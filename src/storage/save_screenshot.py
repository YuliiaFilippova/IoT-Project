import cv2
from datetime import datetime
from utils.paths import SCREENSHOT_DIR


def save_screenshot(frame, event_id):
    filename = f"event_{event_id}.jpg"
    filepath = f"{SCREENSHOT_DIR}/{filename}"
    cv2.imwrite(filepath, frame)
    return filename