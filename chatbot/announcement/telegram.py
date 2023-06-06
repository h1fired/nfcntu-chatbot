from django.conf import settings
from users.models import UserProfile
import io, httpx, asyncio
from PIL import Image
    

def send_broadcast_message(announcement):
    '''Send announcement to all users in telegram bot'''
    
    chat_ids = list(UserProfile.objects.all().values_list('chat_id', flat=True))
    asyncio.run(__fetch(chat_ids, announcement))

async def __fetch(chat_ids, announcement):
    if announcement.preview:
        send_method = 'sendPhoto'
        # image bytes
        photo_bytes = io.BytesIO()
        photo = Image.open(announcement.preview.path)
        photo.save(photo_bytes, format='PNG')
        photo_bytes = photo_bytes.getvalue()
    else:
        send_method = 'sendMessage'
        photo_bytes = None
        
    url = __get_fetch_url(send_method)
    message = __announcement_to_markdown(announcement)
    
    async with httpx.AsyncClient(limits=httpx.Limits(max_connections=30)) as client:
        requests = [client.post(**_get_params(url, id, message, send_method, photo_bytes), timeout=10.0) for id in chat_ids]
        await asyncio.gather(*requests)
        
        
def _get_params(url, chat_id, message, send_method, photo=None):
    params = {
        'url': url,
        'data': __get_data(chat_id, message, send_method)
    }
    if photo is not None:
        params['files'] = {
            'photo': photo
        }
    return params

def __get_fetch_url(send_method):
    return f"{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_TOKEN}/{send_method}"

def __get_data(chat_id, message, send_method):
    message_key = 'text' if send_method == 'sendMessage' else 'caption'
    return {
        'chat_id': chat_id,
        message_key: message,
        'parse_mode': 'Markdown',
    }

def __announcement_to_markdown(announcement):
    title = f'*{announcement.title}*'
    description = announcement.description
    
    return f'{title}\n\n{description}'