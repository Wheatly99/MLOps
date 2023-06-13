import pandas as pd
import numpy as np

np.random.seed(0)

def create_data():
    x = np.linspace(0, 10, 100)
    y = x + np.random.random(100)*2 - 1
    z = x + y + np.random.random(100)*2

    df = pd.DataFrame({'x': x, 'y': y, 'target': z})
    df.to_excel('data/data.xlsx', index=False)

if __name__ == '__main__':
  create_data()