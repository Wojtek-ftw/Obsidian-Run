import polars as pl
df = pl.read_csv("bigfile.csv")
df.groupby("A").agg(pl.col("B").mean())  # 5x+ faster in many use cases
