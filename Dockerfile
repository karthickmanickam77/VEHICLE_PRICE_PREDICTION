FROM python:3.13.9

WORKDIR /app

COPY backend/ /app/backend/
COPY model/ /app/model/

RUN pip install fastapi uvicorn pandas==2.3.3 scikit-learn==1.6.1 joblib pydantic

WORKDIR /app/backend

CMD ["python", "main.py"]