import pandas as pd

df = pd.read_csv("gfgnitsgrstudents.csv")
inactive = df[df["total_score"] == 0]
print(f"Total inactive students: {len(inactive)}")
print(inactive[["name", "total_score"]])
