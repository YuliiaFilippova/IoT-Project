import numpy as np


def detect_daytime(frame):

    brightness = np.mean(frame)

    if brightness < 60:
        return "night"

    return "day"