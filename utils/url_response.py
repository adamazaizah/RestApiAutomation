import requests


class UrlResponse:
    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        self.response = dict()
        for k, v in response.json().items():
            self.response[k] = v
        self.response['status_code'] = response.status_code
        self.response['length'] = len(response.json())