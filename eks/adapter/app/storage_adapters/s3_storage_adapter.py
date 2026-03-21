from config.aws_facade import AWSFacade
from .storage_adapter import StorageAdapter
import os

class S3StorageAdapter(StorageAdapter):
    def __init__(self, bucket_name: str = None):
        self.s3_facade = AWSFacade()
        self.bucket_name = bucket_name

    def get_file_content(self, file_key: str) -> str:
        # Ahora cumple con la interfaz abstracta StorageAdapter
        return self.s3_facade.get_s3_object_content(self.bucket_name, file_key)