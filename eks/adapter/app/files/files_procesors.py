import json
import csv
from files.interfaces import Creator, File

class JSONProcessor(File):
    def parse(self, content):
        data = json.loads(content)
        return {
            "type": "JSON",
            "total_items": len(data),
            "data": [{"key": k, "value": v} for k, v in data.items()]
        }

class CSVProcessor(File):
    def parse(self, content):
        rows = list(csv.reader(content.strip().split("\n")))
        return {
            "type": "CSV",
            "total_items": len(rows),
            "data": rows
        }

class JSONParserFactory(Creator):
    def factory_method(self) -> File:
        return JSONProcessor()

class CSVParserFactory(Creator):
    def factory_method(self) -> File:
        return CSVProcessor()
    

