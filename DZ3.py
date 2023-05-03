'''
import requests


heroes_list = ['Hulk', 'Captain America', 'Vindicator', 'X-Man']
heroes_dict = {}

def comparison_heroes():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url).json()
    for hero in response:
        # print(hero['powerstats'].keys()) # позволяет выбрать характеристику для сравнения
        # print(hero['name']) # позволяет из списка всех героев выбрать нравящихся
        if hero['name'] in heroes_list:
          heroes_dict.setdefault(hero['name'], hero['powerstats']['intelligence'])
    print(f'Лучший показатель по intelligence - {max(heroes_dict, key=heroes_dict.get)}')


if __name__ == '__main__':
    comparison_heroes()
'''
import requests
import os

class YaUploader:
    def init(self, token: str):
        self.token = token
def get_upload_url(self, file_path: str) -> str:
    """Метод получает URL для загрузки файла на Яндекс.Диск"""
    headers = {"Authorization": f"OAuth {self.token}"}
    params = {"path": os.path.basename(file_path), "overwrite": "true"}
    response = requests.get(
        "https://cloud-api.yandex.net/v1/disk/resources/upload",
        headers=headers,
        params=params,
    )
    response.raise_for_status()
    return response.json()["href"]

def upload(self, file_path: str):
    """Метод загружает файлы на яндекс диск"""
    upload_url = self.get_upload_url(file_path)
    with open(file_path, "rb") as f:
        response = requests.put(upload_url, files={"file": f})
    response.raise_for_status()
    if __name__ == '__main__':
        # Получить путь к загружаемому файлу и токен от пользователя
        path_to_file = ...
        token = ...