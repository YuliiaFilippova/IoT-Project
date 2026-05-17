import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    "/opt/homebrew/bin/tesseract"
)

def extract_temperature(frame):

    #roi = frame[0:120, -250:]
    roi = frame[0:120, -120:]

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    return text.strip()