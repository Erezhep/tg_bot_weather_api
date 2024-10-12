# Weather Bot

## Описание

Этот бот на Python, использующий библиотеку `aiogram`, позволяет пользователям получать актуальную информацию о погоде в любом городе. Пользователи могут отправить название города, и бот ответит с данными о текущей погоде.

## Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone <URL_вашего_репозитория>
   cd <имя_папки_репозитория>

2. **Создайте виртуальное окружение (необязательно, но рекомендуется)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # для Linux/Mac
    venv\Scripts\activate  # для Windows
    ```

3. **Установите необходимые зависимости**
   ```bash
    pip install aiogram python-dotenv requests
   ```

4. **Настройте переменные окружения**<br>
   Создайте файл .env в корневом каталоге вашего проекта и добавьте следующие строки
    ```
    BOT_TOKEN=ваш_токен_бота
    WEATHER_API=ваш_API_ключ_погоды
    ```
## Использование

**Запустите бот с помощью следующей команды**

```bash
python bot.py
```

## Команды

- `/start` - Запустите бота и получите приветственное сообщение.
- Отправьте название города (например, "Москва"), чтобы получить информацию о текущей погоде