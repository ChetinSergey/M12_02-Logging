import requests as rq
import logging

#logger = logging.getLogger('RequestsLogger') - из примера

logger_success = logging.getLogger('RequestsLogger_success')
logger_bad = logging.getLogger('RequestsLogger_bad')
logger_blocked = logging.getLogger('RequestsLogger_blocked')

handler = logging.FileHandler('success_responses.log', mode='w', encoding='utf-8')
handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
logger_success.setLevel('INFO')
logger_success.addHandler(handler)

handler = logging.FileHandler('bad_responses.log', mode='w', encoding='utf-8')
handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
logger_bad.setLevel('WARNING')
logger_bad.addHandler(handler)

handler = logging.FileHandler('blocked_responses.log', mode='w', encoding='utf-8')
handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
logger_blocked.setLevel('ERROR')
logger_blocked.addHandler(handler)


sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        status = response.status_code
        print(response)
        if status == 200:
            logger_success.info(f'{site}, response - {status}')
        else:
            logger_bad.warning(f'{site}, response - {status}')

    except (rq.exceptions.ConnectionError, rq.exceptions.Timeout):
        print('ERROR')
        logger_blocked.error(f'{site}, NO CONNECTION')
