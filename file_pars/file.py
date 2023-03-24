import json
import requests


def start(url):

    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)  # Объект библиотеки
    json_data = response.content.decode()  # строка
    print(json_data)

    with open('data.json', 'w') as file:
        json.dump(json_data, file)
