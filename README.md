 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/README.md b/README.md
index a1888606689428f65118edd97503c21d15f35aa1..721c3fdfd558b5227484d077e8f57bbea902b71b 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,30 @@
-# Expert
+# Simple ChatBot Server
+
+Этот проект предоставляет минимальный сервер чат-бота на FastAPI.
+
+## Установка
+
+```bash
+python -m venv .venv
+source .venv/bin/activate
+pip install -r requirements.txt
+```
+
+## Запуск сервера
+
+```bash
+uvicorn app.main:app --reload
+```
+
+После запуска сервер будет доступен на `http://127.0.0.1:8000`.
+
+### Эндпоинты
+
+- `GET /health` — проверка доступности.
+- `POST /chat` — принимает JSON вида `{ "message": "текст", "session_id": "опционально" }` и возвращает ответ чат-бота и историю диалога.
+
+## Тесты
+
+```bash
+pytest
+```
 
EOF
)