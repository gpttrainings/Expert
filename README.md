# Expert
# Simple ChatBot Server

Этот проект предоставляет минимальный сервер чат-бота на FastAPI.

## Установка

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск сервера

```bash
uvicorn app.main:app --reload
```

После запуска сервер будет доступен на `http://127.0.0.1:8000`.

### Эндпоинты

- `GET /health` — проверка доступности.
- `POST /chat` — принимает JSON вида `{ "message": "текст", "session_id": "опционально" }` и возвращает ответ чат-бота и историю диалога.

## Тесты

```bash
pytest
```
