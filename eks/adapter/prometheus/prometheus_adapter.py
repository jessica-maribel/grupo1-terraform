# prometheus_adapter.py
from fastapi import FastAPI
from prometheus_client import start_http_server, Counter, generate_latest, CONTENT_TYPE_LATEST
import json
import time
import threading
import os

app = FastAPI()

REQUESTS_COUNTER = Counter('parsed_files_total', 'Total parsed files', ['file_type'])

log_path = "/var/log/app/adapter-app.log"

def tail_logfile(path):
    with open(path, 'r') as file:
        file.seek(0, os.SEEK_END)  # Move to EOF
        while True:
            line = file.readline()
            if line:
                try:
                    log_entry = json.loads(line.strip())
                    if log_entry.get('event') == 'file_parsed':
                        file_type = log_entry.get('file_type', 'unknown')
                        REQUESTS_COUNTER.labels(file_type=file_type).inc()
                except json.JSONDecodeError:
                    pass
            else:
                time.sleep(1)

@app.get("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    threading.Thread(target=tail_logfile, args=(log_path,), daemon=True).start()
    start_http_server(9200)
    while True:
        time.sleep(5)