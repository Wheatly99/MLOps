from fastapi import FastAPI, UploadFile
import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'MLOps project'}

@app.post("/file")
def upload_file(file: UploadFile):

    df = pd.read_excel(file.file.read())
    X = df[['x', 'y']]
    y = df.target

    model = joblib.load('model.pkl')

    return print(f'MSE = {mean_squared_error(model.predict(X), y)}')