FROM python:3.9-slim

WORKDIR /app
COPY synthetic_data.py /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
CMD ["python", "synthetic_data.py"]