import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        data_list = []
        data_collection = json.loads(self.get_response_body())
        for data in data_collection:
            data_list.append(data)
            
        return data_list

people = GetRequester("https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json")
# collections = people.get_response_body()
# print(collections)
collections = people.load_json()
for collection in (collections):
    print(collection)