import cv2
from datetime import datetime

from utils.paths import SCREENSHOT_DIR


def save_screenshot(frame):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = f"event_{timestamp}.jpg"

    filepath = f"{SCREENSHOT_DIR}/{filename}"

    cv2.imwrite(filepath, frame)

    #return filepath
    return filename