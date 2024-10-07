import unittest
import requests


class BaseApiClass(unittest.TestCase):
    BASE_URL = "https://fastapi.dev.tasleem.creativeadvtech.ml/api/v1"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    def setUp(self):
        # Add any setup logic here, such as setting up test data
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.session.timeout = (5, 15)

    def get(self, endpoint, params=None):
        return self.session.get(f"{self.BASE_URL}{endpoint}", params=params)

    def post(self, endpoint, data=None, json=None):
        return self.session.post(f"{self.BASE_URL}{endpoint}", data=data, json=json)

    def put(self, endpoint, data=None, json=None):
        return self.session.put(f"{self.BASE_URL}{endpoint}", data=data, json=json)

    def delete(self, endpoint):
        return self.session.delete(f"{self.BASE_URL}{endpoint}")

    def tearDown(self):
        # Conditional cleanup
        if hasattr(self, 'session') and self.session:
            self.session.close()
        super().tearDown()
