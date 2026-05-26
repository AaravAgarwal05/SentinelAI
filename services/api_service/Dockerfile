FROM python:3.13-slim

WORKDIR /app

COPY services/api_service/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "services.api_service.api_service:app", "--host", "0.0.0.0", "--port", "8000"]
