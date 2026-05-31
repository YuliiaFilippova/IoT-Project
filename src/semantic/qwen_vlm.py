from transformers import Qwen2VLForConditionalGeneration
from transformers import AutoProcessor

from PIL import Image

import torch


MODEL_NAME = "Qwen/Qwen2-VL-2B-Instruct"

device = "mps" if torch.backends.mps.is_available() else "cpu"


model = Qwen2VLForConditionalGeneration.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if device == "mps" else torch.float32
).to(device)


processor = AutoProcessor.from_pretrained(MODEL_NAME)

def analyze_frames(frame_paths):
    prompt = """
Analyze this wildlife feeder image.

Describe only:

- animal species and their count (IMPORTANT)
- behavior (feeding, resting, moving or aggressive)
- interaction (none, peaceful, competitive or fighting)
- overall activity level (low, medium or high)
- weather conditions (rain, snow, clear)

Use only clearly visible information.

Output ONE SHORT sentence.
"""

    images = []

    for path in frame_paths:

        img = Image.open(path).convert("RGB")

        # IMPORTANT
        img = img.resize((512, 512))

        images.append(img)

    messages = [
        {
            "role": "user",
            "content": [
                *[
                    {
                        "type": "image",
                        "image": img
                    }
                    for img in images
                ],
                {
                    "type": "text",
                    "text": prompt
                }
            ]
        }
    ]

    text = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = processor(
        text=[text],
        images=images,
        return_tensors="pt"
    ).to(device)

    with torch.no_grad():

        output = model.generate(
            **inputs,
            max_new_tokens=60,
            do_sample=False,
            repetition_penalty=1.1,
            no_repeat_ngram_size=3,
            eos_token_id=processor.tokenizer.eos_token_id,
            pad_token_id=processor.tokenizer.eos_token_id
        )

    generated_ids = output[0][inputs.input_ids.shape[1]:]

    response = processor.decode(
        generated_ids,
        skip_special_tokens=True
    )

    #print(response)
    return response