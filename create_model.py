from sklearn.linear_model import LinearRegression
import pandas as pd
import joblib

def train_linear_model():

  df = pd.read_excel('data/data.xlsx')
  X = df[['x', 'y']]
  y = df.target

  model = LinearRegression()
  model.fit(X, y)
  joblib.dump(model, 'model.pkl')

if __name__ == '__main__':
  train_linear_model()