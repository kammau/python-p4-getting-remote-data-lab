import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url
        self.get_response_body()

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        data_list = []
        data_info = json.loads(self.get_response_body())
        for data in data_info:
            data_list.append(data)
        
        return data_list