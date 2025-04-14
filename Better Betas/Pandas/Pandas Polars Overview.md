# Pandas and Polars Overview

## Scripts
[download.py](./download.py): downloads the [Massive-Yahoo-Finance-Dataset](https://www.kaggle.com/datasets/iveeaten3223times/massive-yahoo-finance-dataset) from Kaggle.
[benchmark_memory.py](./benchmark_memory.py): prints memory usage for pandas vs polars on the yahoo dataset.
[benchmark_timing.py](./benchmark_timing.py): prints timing estimates for loading the yahoo dataset in pandas vs polars.


## Loading Time
Polars generally has a longer loading time compared to Pandas, especially for large datasets. This is partly due to its schema inference process. In some cases, Polars can misidentify column types during import, leading to errors or incorrect data representations. This issue can be mitigated by setting the infer_schema_length=None parameter when reading CSV files, which forces Polars to scan the entire file to better infer data types.

| Operation         | Duration (seconds) |
|------------------|--------------------|
| Pandas Load      | 4.86817            |
| Polars Load      | 17.48769           |

## Schema Inference and Type Handling
While Pandas defaults to eager loading with relatively straightforward type inference, Polars takes a more nuanced approach. Its default behavior uses a sample of rows to guess the schema, which is faster but less robust. Specifying schema manually or using infer_schema_length=None allows for better type detection at the cost of performance during initial load.

## Memory Usage
Polars typically has a smaller memory footprint upon initial load because it employs lazy evaluation. This means data is not immediately processed or loaded into memory—computations are deferred until explicitly requested (e.g., when calling .collect() or converting to a DataFrame). This makes Polars particularly efficient when chaining multiple operations, as it can optimize the execution plan before actually doing any computation.

Pandas, on the other hand, loads all data eagerly and holds it in memory, which can lead to higher memory consumption. However, memory usage in Pandas can be significantly reduced by optimizing data types—for instance, converting object columns to categorical types when appropriate. This is conceptually similar to compressing data, akin to zipping a file, and can lead to large memory savings without loss of information.


| Configuration           | Current Memory Usage | Peak Memory Usage | Estimated Size |
|-------------------------|----------------------|-------------------|----------------|
| Pandas Default          | 41.87 MB             | 138.50 MB         | 113.94 MB      |
| Pandas Column Optimized | 34.74 MB             | 138.37 MB         | 34.68 MB       |
| Polars Default          | 0.01 MB              | 0.02 MB           | 48.38 MB       |
| Polars Forced Load      | 72.08 MB             | 72.08 MB          | 48.38 MB       |
