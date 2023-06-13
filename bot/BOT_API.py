import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("api_key")  # API ключ для отримання доступу до даних
server = 'polygrid.store'
headers = {
    'Accept': 'application/json',  # Тип даних
    'Authorization': f'ApiKey {api_key}'  # Вставка API ключа в заголовок запиту
}


def get_specialty():
    '''Функція яка повертає всі спеціальності'''
    url = f'http://{server}/api/specialty/'
    request = requests.get(url=url, headers=headers)  # Запит до API
    result = request.json()
    return result


def get_group():
    '''Функція яка повертає всі групи'''
    url = f'http://{server}/api/groups/'
    request = requests.get(url=url, headers=headers)  # Запит до API
    result = request.json()
    return result


def post_user(data):
    '''Функція яка створює користувача на сервері'''
    # Дані запиту
    url = f'http://{server}/api/users/'
    # Заголовки запиту
    request = requests.post(url=url, data=data, headers=headers)  # Запит до API


def get_schedule(group, day):
    '''Функція яка повертає розклад'''
    url = f'http://{server}/api/schedule/'
    if group is None:
        url += f'?day={day}'
    if day is None:
        url += f'?group={group}'
    if day and group:
        url += f'?group={group}&day={day}'

    request = requests.get(url=url, headers=headers)
    return request.json()