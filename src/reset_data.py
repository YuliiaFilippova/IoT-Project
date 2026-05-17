import os
import shutil

from utils.paths import (
    SCREENSHOT_DIR,
    PROCESSED_DIR,
    JSON_DIR,
    SEMANTIC_JSON_DIR,
    CSV_DIR
)


def clear_folder(folder_path):

    for filename in os.listdir(folder_path):

        file_path = os.path.join(
            folder_path,
            filename
        )

        try:

            if os.path.isfile(file_path):
                os.remove(file_path)

            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

        except Exception as e:

            print(f"Failed deleting {file_path}")
            print(e)


print("Clearing old experiment data...")

clear_folder(SCREENSHOT_DIR)

clear_folder(PROCESSED_DIR)

clear_folder(JSON_DIR)

clear_folder(SEMANTIC_JSON_DIR)

clear_folder(CSV_DIR)

print("Reset complete.")