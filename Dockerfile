FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY AdvanceCalculater.py .
COPY webapp.py .

CMD ["python", "webapp.py"]