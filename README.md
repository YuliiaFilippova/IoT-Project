# Wildlife Analytics Pipeline

This project explores how multimodal AI systems can transform raw wildlife livestreams into structured semantic data suitable for ecological monitoring and behavioral analysis.

---
## Features

- Real-time YouTube livestream processing
- Wildlife detection with YOLOv8
- Event-driven frame extraction
- Temporal filtering to avoid duplicate detections
- Semantic scene analysis using Qwen2-VL
- Structured JSON and CSV telemetry generation
- Livestream timestamp extraction via OCR
- Live monitoring interface with detection overlays

---

## Pipeline

```text
Livestream
→ YOLO Detection
→ Trigger Logic
→ Frame Extraction
→ Semantic Analysis
→ Structured Telemetry
```
---

## Example Output
```text
{
  "species": [
    {
      "name": "pheasant",
      "count": 2
    },
    {
      "name": "pigeon",
      "count": 1
    }
  ],
  "dominant_species": "pheasant",
  "behavior": "feeding",
  "interaction": "peaceful",
  "activity_level": "medium",
  "summary": "Two pheasants and a pigeon are feeding peacefully from a wooden bird feeder.The overall activity level is medium.",
  "timestamp": "2026-05-17 18:48:09.423705",
  "source_image": "event_20260517_184759.jpg",
  "event": "species_change"
  "daytime": "day",
  "temperature": "11°C",
  
}
```

---

## Tech Stack
- Python
- OpenCV
- YOLOv8
- Qwen2-VL
- Ollama
- Pandas
- Pytesseract
- FFmpeg
- yt-dlp

---

## Current Limitations
- Livestream latency depends on hardware performance
- Lightweight detector may occasionally miss animals
- OCR timestamp extraction is not always perfect
- Analytics layer is still under development

---

## Future Work
- Statistical analysis of collected telemetry
- Wildlife activity visualization
- Object tracking
- Database integration
- Real-time analytics dashboard
- #### Demo: A short demonstration video with a system walkthrough and live detection examples will be added soon.

---

## Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```
2. Start live collection:

```bash
python src/collect_live_data.py
```

3. Run semantic analysis:

```bash
python src/analyze_events.py
```

---

## Author

### Yuliia Filippova
