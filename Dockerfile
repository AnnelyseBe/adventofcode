# Dit is de dockerfile die wordt gebruikt als environment voor Python
FROM python:3.10-slim

# Installeer git
RUN apt-get update && apt-get install -y git

# Kopieer het bestand requirements.txt naar de container
COPY requirements.txt requirements.txt

# Installeer alle benodigde pakketten
RUN pip install --no-cache-dir -r requirements.txt