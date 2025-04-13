FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY firehose_processor.py .

CMD ["python", "firehose_processor.py"]
