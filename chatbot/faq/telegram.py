import requests
from django.conf import settings

def send_answer(chat_id, question, answer):
    '''Send an answer to a telegram user's question'''
    
    data = {
        'chat_id': chat_id,
        'text': _message_to_answer(question, answer),
        'parse_mode': 'Markdown',
    }
    
    request = requests.post(url=_get_fetch_url(), data=data)
    return request.status_code

def _get_fetch_url():
    return f'{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/sendMessage'

def _message_to_answer(question, message):
    return f'*Відповідь на запитання "{question}":*\n\n{message}'