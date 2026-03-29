# Effective Mobile - Веб-приложение с Nginx и Docker

Простое веб-приложение, состоящее из backend-сервера на Python и reverse proxy на базе Nginx, развернутых в Docker-контейнерах.

## 📋 Описание

Проект демонстрирует базовую архитектуру микросервиса с использованием:
- **Backend** - HTTP-сервер на Python (порт 8080)
- **Nginx** - Reverse proxy (порт 80)

## 🏗️ Архитектура

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   Пользо-   │ ───► │    Nginx    │ ───► │   Backend   │
│   ватель    │      │  (порт 80)  │      │  (порт 8080)│
│  (curl)     │      │             │      │   (Python)  │
└─────────────┘      └─────────────┘      └─────────────┘
     localhost              │                     │
                          Docker Network (app-network)
```

### Схема взаимодействия:

1. Пользователь отправляет HTTP-запрос на `http://localhost`
2. Nginx принимает запрос на порту 80
3. Nginx проксирует запрос на backend-сервис через внутреннюю Docker-сеть
4. Backend обрабатывает запрос и возвращает ответ: "Hello from Effective Mobile!"
5. Nginx возвращает ответ пользователю

## 🚀 Технологии

- **Docker** - контейнеризация приложений
- **Docker Compose** - оркестрация многоконтейнерных приложений
- **Python 3.11** - backend-сервер (http.server)
- **Nginx (Alpine)** - reverse proxy
- **Docker Network** - изолированная сеть между сервисами

## 📁 Структура проекта

```
effective mobile/
├── backend/
│   ├── Dockerfile          # Dockerfile для Python-приложения
│   └── app.py              # HTTP-сервер на Python
├── nginx/
│   └── nginx.conf          # Конфигурация Nginx
├── docker-compose.yml      # Оркестрация контейнеров
├── README.md               # Документация
└── .gitignore              # Игнорируемые файлы Git
```

## ⚙️ Установка и запуск

### Требования

- Docker (версия 20.10+)
- Docker Compose (версия 2.0+)

### Запуск проекта

1. Убедитесь, что порт 80 свободен на вашем хосте
2. Перейдите в директорию проекта:
   ```bash
   cd "/home/lexx/Documents/effective mobile"
   ```

3. Запустите контейнеры:
   ```bash
   docker-compose up -d --build
   ```

   Флаги:
   - `-d` - запуск в фоновом режиме
   - `--build` - принудительная пересборка образов

4. Проверьте статус контейнеров:
   ```bash
   docker-compose ps
   ```

   Оба контейнера должны быть в статусе `healthy`:
   - `effective-mobile-backend`
   - `effective-mobile-nginx`

## ✅ Проверка работоспособности

### Основная проверка

Выполните команду:
```bash
curl http://localhost
```

**Ожидаемый ответ:**
```
Hello from Effective Mobile!
```

### Дополнительные проверки

1. **Проверка health endpoint backend:**
   ```bash
   docker exec effective-mobile-backend python -c "import urllib.request; print(urllib.request.urlopen('http://localhost:8080/health').read().decode())"
   ```

2. **Проверка health endpoint nginx:**
   ```bash
   curl http://localhost/nginx-health
   ```

3. **Просмотр логов backend:**
   ```bash
   docker-compose logs backend
   ```

4. **Просмотр логов nginx:**
   ```bash
   docker-compose logs nginx
   ```

## 🔧 Управление проектом

### Остановка проекта
```bash
docker-compose down
```

### Остановка с удалением томов
```bash
docker-compose down -v
```

### Перезапуск
```bash
docker-compose restart
```

### Пересборка и запуск
```bash
docker-compose up -d --build --force-recreate
```

### Просмотр логов в реальном времени
```bash
docker-compose logs -f
```

## 🔒 Безопасность

В проекте реализованы следующие меры безопасности:

1. **Запуск от не-root пользователя** - backend приложение запускается от имени пользователя `appuser` (UID 1000)
2. **Изолированная Docker-сеть** - backend недоступен извне, только через nginx
3. **Минимальные образы** - используется `python:3.11-slim` и `nginx:alpine`
4. **Health checks** - автоматическая проверка здоровья сервисов
5. **Нет проброса лишних портов** - наружу проброшен только порт 80 nginx

## 📝 Конфигурация

### Backend (порт 8080)

- Обрабатывает GET-запросы на `/` и `/health`
- Возвращает текст: "Hello from Effective Mobile!"
- Логирование в stderr

### Nginx (порт 80)

- Проксирует все запросы на backend
- Передает заголовки:
  - `Host`
  - `X-Real-IP`
  - `X-Forwarded-For`
  - `X-Forwarded-Proto`
- Имеет собственный health endpoint `/nginx-health`

## 🐛 Решение проблем

### Порт 80 занят
Если порт 80 занят другим приложением (например, Apache или другим nginx):

1. Найдите процесс:
   ```bash
   sudo lsof -i :80
   ```

2. Остановите конфликтующий сервис или измените порт в `docker-compose.yml`:
   ```yaml
   ports:
     - "8080:80"  # Используйте другой порт
   ```

### Контейнеры не запускаются
Проверьте логи:
```bash
docker-compose logs
```

### Backend недоступен
Убедитесь, что backend запустился:
```bash
docker-compose ps
docker-compose logs backend
```

## 📄 Лицензия

Проект создан в учебных целях.

## 👤 Автор

Effective Mobile - тестовое задание

---

**Дата создания:** 29 марта 2026  
**Версия проекта:** 1.0
