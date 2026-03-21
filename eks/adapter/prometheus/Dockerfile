FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY prometheus_adapter.py /app/

EXPOSE 9200

CMD ["python", "prometheus_adapter.py"]