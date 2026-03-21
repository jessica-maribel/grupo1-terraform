import os
from storage_adapters.storage_adapter import StorageAdapter
from storage_adapters.s3_storage_adapter import S3StorageAdapter
from storage_adapters.local_storage_adapter import LocalStorageAdapter

def get_storage_adapter(bucket_or_path) -> StorageAdapter:
    adapter_type = os.getenv("STORAGE_TYPE", "s3")
    if adapter_type == "s3":
        return S3StorageAdapter(bucket_or_path)
    elif adapter_type == "local":
        return LocalStorageAdapter(base_path=bucket_or_path)
    else:
        raise ValueError(f"Tipo de almacenamiento no soportado: {adapter_type}")