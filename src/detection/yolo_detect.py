import cv2

from ultralytics import YOLO


#model = YOLO("yolov8n.pt") #nano model, very small, very fast, but weak
model = YOLO("yolov8s.pt") # fast, good accuracy
#model = YOLO("yolov8m.pt") # medium speed, better accuracy
#model = YOLO("yolov8l/x.pt") # heavy speed, strong accuracy

IGNORE_CLASSES = [
    "bench",
    "chair",
    "person",
    "bottle",
    "cup",
    "tv",
    "laptop"
]


def detect_animals(frame):

    results = model(frame)

    detections = []

    animal_count = 0

    annotated_frame = frame.copy()

    for result in results:

        for box in result.boxes:

            cls_id = int(box.cls[0])

            class_name = model.names[cls_id]

            confidence = float(box.conf[0])

            # ignore unwanted classes
            if class_name in IGNORE_CLASSES:
                continue

            # confidence threshold
            if confidence < 0.6:
                continue

            animal_count += 1

            detections.append({
                "class": class_name,
                "confidence": round(confidence, 2)
            })

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            # DRAW BOX
            cv2.rectangle(
                annotated_frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            label = f"{class_name} {confidence:.2f}"

            cv2.putText(
                annotated_frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

    return {
        "animal_count": animal_count,
        "detections": detections,
        "annotated_frame": annotated_frame
    }