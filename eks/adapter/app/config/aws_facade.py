import os
import boto3

class AWSFacade:
    _s3 = None
    _secrets_manager = None

    def __init__(self):
        endpoint = os.getenv('AWS_ENDPOINT_URL')
        if endpoint:
            self._s3 = boto3.client('s3', endpoint_url=endpoint)
            self._secrets_manager = boto3.client('secretsmanager', endpoint_url=endpoint)
        else:
            self._s3 = boto3.client('s3')
            self._secrets_manager = boto3.client('secretsmanager')

    # método para obtener contenido de S3
    def get_s3_object_content(self, bucket_name, file_key):
        response = self._s3.get_object(Bucket=bucket_name, Key=file_key)
        return response['Body'].read().decode('utf-8')

    # método para obtener un secreto completo
    def get_secret(self, secret_name):
        response = self._secrets_manager.get_secret_value(SecretId=secret_name)
        secret_string = response['SecretString']
        return secret_string