import requests
import os

api_key = 'GXt06XrBo1RLtC_WSYZ63w' # API ключ для отримання доступу до даних
server = 'polygrid.store'
headers = {
    'Accept': 'application/json', # Тип даних
    'Authorization': f'ApiKey {api_key}' # Вставка API ключа в заголовок запиту
}

def get_specialty():
    '''Функція яка повертає всі спеціальності'''
    url = f'http://{server}/api/specialty/'
    request = requests.get(url=url, headers=headers)  # Запит до API

    result = request.json()
    return result

def get_group():
    '''Функція яка поаертає всі групи'''
    url = f'http://{server}/api/groups/'
    request = requests.get(url=url, headers=headers)  # Запит до API
    result = request.json()
    return result

def post_user(data):
    '''Функція яка створює користувача на сервері'''
    # Дані запиту
    url = f'http://{server}/api/users/'
    # Заголовки запиту
    headers = {
        'Accept': 'application/json',  # Тип даних
        'Authorization': f'ApiKey {api_key}'  # Вставка API ключа в заголовок запиту
    }
    request = requests.post(url=url, data=data, headers=headers)  # Запит до API

