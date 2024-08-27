# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы в контейнер
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY data.csv data.csv

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Команда для запуска приложения
CMD ["python", "app.py"]