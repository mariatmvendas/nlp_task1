FROM python:3.11-alpine

WORKDIR /app_v2

COPY mainv2.py /app_v2/mainv2.py
COPY requirements_v2.txt /app_v2/requirements_v2.txt

RUN pip install --no-cache-dir -r requirements_v2.txt

EXPOSE 8000

CMD ["uvicorn", "mainv2:app_v2", "--host", "0.0.0.0", "--port", "8000"] 