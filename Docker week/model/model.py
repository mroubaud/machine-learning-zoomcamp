import pandas as pd
import numpy as np

data="fsa-headcount-as-at-31-january-2018.csv"
df = pd.read_csv(data)
print(df.describe)