FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY firehose_publisher.py .

CMD ["python", "firehose_publisher.py"]
