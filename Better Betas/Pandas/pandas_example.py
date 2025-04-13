import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(1_000_000, 5), columns=list('ABCDE'))
result = df.groupby('A').agg({'B': 'mean'})  # Simple, but slow on large scale
