import pandas as pd

df = pd.read_csv("gfgnitsgrstudents.csv")
top_10 = df.sort_values(by="total_score", ascending=False).head(10)
print("Top 10 Performers:")
print(top_10[["name", "total_score"]])
