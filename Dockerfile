FROM python:3.12-slim

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App source
COPY . .

# Data directory
RUN mkdir -p /app/data

EXPOSE 8000

ENV GOV_DB=/app/data/gov_sites.db
ENV PORT=8000
ENV DEBUG=0

CMD ["python", "-m", "app.main"]

