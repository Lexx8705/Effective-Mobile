# Используем минимальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Создаем пользователя для запуска приложения (не root)
RUN useradd -m -u 1000 appuser

# Копируем приложение
COPY app.py .

# Меняем владельца файла на пользователя appuser
RUN chown appuser:appuser app.py

# Переключаемся на пользователя appuser
USER appuser

# Документируем порт (не публикует его автоматически)
EXPOSE 8080

# Запускаем приложение
CMD ["python", "app.py"]
