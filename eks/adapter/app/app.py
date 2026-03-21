# app.py (FastAPI)
from fastapi import FastAPI, HTTPException
from files.storage_adapter import get_storage_adapter
from files.parser import get_parser_factory
from config.config_manager import ConfigManager
import logging
import json

app = FastAPI()

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("/var/log/app/adapter-app.log")
logger.addHandler(file_handler)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/parse-file/")
def parse_file(payload: dict):
    bucket_or_path = payload.get('bucket')
    file_key = payload.get('key')

    if not file_key:
        raise HTTPException(status_code=400, detail="key is required")

    parser_factory = get_parser_factory(file_key)
    parser = parser_factory.factory_method()

    storage_adapter = get_storage_adapter(bucket_or_path)
    content = storage_adapter.get_file_content(file_key)

    result = parser.parse(content)

    config_manager = ConfigManager()
    secret_content = config_manager.get_secret()

    # Log the parsing event as JSON
    logger.info(json.dumps({
        'event': 'file_parsed',
        'file_key': file_key,
        'file_type': result.get('type'),
        'total_items': result.get('total_items')
    }))

    return {
        'parsed_content': result,
        'secret_content': secret_content
    }