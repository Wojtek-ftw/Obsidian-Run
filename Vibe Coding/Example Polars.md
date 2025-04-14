# Polars LLM Request
## Overview
As I am more of a pandas user than polars, I'm not too familiar with the syntax. However, I'm familiar with the generaly process of filtering datasets based on criteria, and that most filtering schemes assume data types and structures are consistent.
So, I asked ChatGPT to help filter my `df` based on whether it's numeric or not, so that I may do the appropriate identity operation on the data.

## Request
```
import polars as pl

df = pl.read_csv("your_file.csv")

df = df.with_columns([
    pl.when(pl.col(col).is_numeric())
      .then(pl.col(col) + 0)
      .otherwise(pl.col(col).cast(pl.Utf8) + "")
      .alias(col)
    for col in df.columns
])
```

## Result
I reached an error:
```
AttributeError: 'Expr' object has no attribute 'is_numeric'
```

## Explanation
Earlier in the request, I asked for a similar deal leveraging pandas. 
A compounding details that may have led to this:
1. I believe the LLM mistaken that polars had `is_numeric` due to the request's proximity to pandas related quieries.
2. Incorrect suggestion from online forums, causing mis training data.
3. Version changes. While not relevant directly to this example, I've come across this issue with pandas before.

## Fix
Exhuastively check if the column schema is a numeric_type.
```
import polars as pl

df = pl.read_csv("your_file.csv")

numeric_types = [pl.Int8, pl.Int16, pl.Int32, pl.Int64,
                 pl.UInt8, pl.UInt16, pl.UInt32, pl.UInt64,
                 pl.Float32, pl.Float64]

df = df.with_columns([
    (pl.col(col) + 0 if df.schema[col] in numeric_types else pl.col(col).cast(pl.Utf8) + "")
    .alias(col)
    for col in df.columns
])
```