import ollama
import json

def build_semantic_state(vlm_output):
    prompt = f"""
You are an AI wildlife analytics system.

Convert the following wildlife observation into structured JSON.

Observation:
{vlm_output}

Return ONLY JSON.

Use this schema:

{{
  "species": [
    {{
      "name": "species",
      "count": count
    }}
  ],

  "dominant_species": "species",

  "behavior": "feeding" or "resting" or "moving" or "aggressive",

  "interaction": "none" or "peaceful" or "competitive" or "fighting",

  "activity_level": "low" or "medium" or "high",
  
  "weather": "rain" or "snow" or "clear"


  "summary": "short summary"
}}
"""

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"]

    try:

        return json.loads(content)

    except Exception:

        return {

            "species": [],

            "dominant_species": "unknown",

            "behavior": "unknown",

            "interaction": "unknown",

            "activity_level": "unknown",

            "summary": content
        }