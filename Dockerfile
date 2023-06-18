FROM python:3.10
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY model.pkl ./model.pkl
COPY api.py ./api.py
CMD ["uvicorn", "api:app", "--host", "127.0.0.1", "--port", "8000"]
