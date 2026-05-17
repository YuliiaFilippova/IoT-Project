import os
import json

from datetime import datetime


def save_json(data, output_dir):

    os.makedirs(output_dir, exist_ok=True)

    filename = datetime.now().strftime(
        "%Y%m%d_%H%M%S.json"
    )

    filepath = os.path.join(
        output_dir,
        filename
    )

    with open(filepath, "w") as f:

        json.dump(
            data,
            f,
            indent=4
        )