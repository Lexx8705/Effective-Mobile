#!/usr/bin/env python3
"""
Простой HTTP-сервер для Effective Mobile
Отвечает на / текстом: "Hello from Effective Mobile!"
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import sys


class EffectiveMobileHandler(BaseHTTPRequestHandler):
    """Обработчик HTTP-запросов"""

    def do_GET(self):
        """Обрабатывает GET-запросы"""
        if self.path == '/' or self.path == '/health':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'Hello from Effective Mobile!')
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'Not Found')

    def log_message(self, format, *args):
        """Логирует сообщения в стандартный вывод"""
        sys.stderr.write(f"[Backend] {args[0]} - {args[1]}\n")


def main():
    """Запускает HTTP-сервер на порту 8080"""
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, EffectiveMobileHandler)
    print("[Backend] Сервер запущен на порту 8080...")
    sys.stdout.flush()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[Backend] Остановка сервера...")
        httpd.shutdown()


if __name__ == '__main__':
    main()
