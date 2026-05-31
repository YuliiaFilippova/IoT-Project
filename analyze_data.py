import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("species_observations.csv")
print(df.head(10))

SPECIES_MAP = {

    # Pigeons
    #"Pigeon": "pigeon",
    "gray pigeon": "pigeon",
    "grey pigeon": "pigeon",
    "blue pigeon": "pigeon",
    "wood pigeon": "pigeon",

    # Crows
    #"Crow": "crow",
    "crows": "crow",

    # Blackbirds
    #"Blackbird": "blackbird",
    "black bird": "blackbird",

    # Woodpeckers
    "Spotted Woodpecker": "woodpecker",
    "Great Spotted Woodpecker": "woodpecker",
    "great spotted woodpecker": "woodpecker",

    # Generic birds
    "bird": "unidentified_bird",
    "white bird": "unidentified_bird",
    "grey bird": "unidentified_bird",
    "gray bird": "unidentified_bird",
    "bird with orange beak": "unidentified_bird",
    "bird with yellow beak": "unidentified_bird",
    "black bird with white spots": "unidentified_bird",
    "black with orange beak": "unidentified_bird",
    "blue-grey with yellow beak": "unidentified_bird",

    # Squirrels
    "ground squirrel": "squirrel",
}

df["species"] = (
    df["species"]
    .str.strip()
    .replace(SPECIES_MAP)
    .str.lower()
)

BAD_LABELS = [
    "animal",
    "wild animal",
    "unknown"
]

df = df[~df["species"].isin(BAD_LABELS)]

print(df["species"].value_counts())

species_counts = df["species"].value_counts()#.head(10)
species_counts.plot(kind="barh")
plt.title("Species Distribution")
plt.ylabel("Observations")
plt.show()

#print(df["behavior"].value_counts())

#behavior_counts = df["behavior"].value_counts()#.head(10)
#behavior_counts.plot(kind="barh")
#plt.title("Behavior Distribution")
#plt.ylabel("Observations")
#plt.show()

#print(df["interaction"].value_counts())

#interaction_counts = df["interaction"].value_counts()#.head(10)
#interaction_counts.plot(kind="barh")
#plt.title("Interaction Distribution")
#plt.ylabel("Observations")
#plt.show()