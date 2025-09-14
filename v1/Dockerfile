FROM python:3.11-alpine

WORKDIR /app_v1

COPY mainv1.py /app_v1/mainv1.py
COPY requirements_v1.txt /app_v1/requirements_v1.txt

RUN pip install --no-cache-dir -r requirements_v1.txt

EXPOSE 8000

CMD ["uvicorn", "mainv1:app_v1", "--host", "0.0.0.0", "--port", "8000"] 