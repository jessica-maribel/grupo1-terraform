from files.files_procesors import JSONParserFactory, CSVParserFactory

def get_parser_factory(file_key: str):
    if file_key.endswith(".json"):
        return JSONParserFactory()
    elif file_key.endswith(".csv"):
        return CSVParserFactory()
    else:
        raise ValueError(f"No parser for file: {file_key}")
