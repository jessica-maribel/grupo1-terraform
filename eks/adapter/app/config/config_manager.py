import time
import os
import json
from config.aws_facade import AWSFacade 

class ConfigManager:
    _instance = None
    _secrets_loaded = False
    _aws_facade = None
    _last_load_time = 0
    _cache_ttl = 120  # 2 minutos

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._aws_facade = AWSFacade()  # usando facade
        return cls._instance

    def load_secrets(self):
        secret_id = os.getenv('SECRET_NAME')
        secret_string = self._aws_facade.get_secret(secret_id)
        self._secrets = json.loads(secret_string)
        self._secrets_loaded = True
        self._last_load_time = time.time()

    def get_secret(self, key=None):
        current_time = time.time()
        if (not self._secrets_loaded) or (current_time - self._last_load_time > self._cache_ttl):
            self.load_secrets()

        if key:
            return self._secrets.get(key, None)
        else:
            return self._secrets