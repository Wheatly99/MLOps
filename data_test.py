import pandas as pd
import numpy as np

np.random.seed(0)

x = np.linspace(2, 8, 100)
y = x + np.random.random(100) - 1
z = x + y + np.random.random(100)

df = pd.DataFrame({'x': x, 'y': y, 'target': z})
df.to_excel('test/data.xlsx', index=False)