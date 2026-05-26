FROM python:3.13-slim

WORKDIR /app

COPY services/incident_worker/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["python", "-m", "services.incident_worker.consumer"]
