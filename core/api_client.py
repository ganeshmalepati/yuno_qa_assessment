import requests

class ApiClient:

    def post(self, url, headers, body):
        return requests.post(url, json=body, headers=headers)

    def get(self, url, headers):
        return requests.get(url, headers=headers)
