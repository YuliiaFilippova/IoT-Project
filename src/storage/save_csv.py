import pandas as pd
import os

from utils.paths import CSV_DIR


CSV_PATH = os.path.join(
    CSV_DIR,
    "wildlife_log.csv"
)


def save_csv(row):

    df = pd.DataFrame([row])

    if os.path.exists(CSV_PATH):

        df.to_csv(
            CSV_PATH,
            mode='a',
            header=False,
            index=False
        )

    else:

        df.to_csv(
            CSV_PATH,
            index=False
        )