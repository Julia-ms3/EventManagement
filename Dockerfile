FROM python:3.11-slim

# Папка, де лежить manage.py
WORKDIR /app

# Копіюємо тільки потрібну частину
COPY ./event_manager /app

# Встановлюємо залежності
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Відкриваємо порт
EXPOSE 8000

# Запускаємо Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]