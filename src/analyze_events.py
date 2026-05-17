import time

from semantic.semantic_pipeline import (
    run_semantic_pipeline
)


while True:

    run_semantic_pipeline()

    time.sleep(10)