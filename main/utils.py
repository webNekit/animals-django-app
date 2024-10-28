import requests
import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

def send_message_to_telegram(message):
    # Получите токен и chat_id из настроек
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')

    # Формируем URL для отправки сообщения
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    # Формируем данные для запроса
    data = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'  # Опционально, если хотите использовать HTML-разметку
    }

    # Отправляем POST-запрос
    response = requests.post(url, data=data)

    # Проверяем, успешен ли запрос
    if response.status_code != 200:
        print(f"Ошибка отправки сообщения: {response.status_code} - {response.text}")
