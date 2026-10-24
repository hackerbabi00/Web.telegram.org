import os
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = "8701172141:AAFMdy7UC6bqb4CGXdaHhm2KQXWPpZ25-U4"
CHAT_ID = "8701172141"


def get_client_ip():
    if request.headers.get('X-Forwarded-For'):
        return request.headers.get('X-Forwarded-For').split(',')[0].strip()
    return request.remote_addr


@app.route('/health')
def health():
    return "OK", 200


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    ip = get_client_ip()
    ua = request.headers.get('User-Agent', 'Bilinmiyor')
    lang = request.headers.get('Accept-Language', 'Bilinmiyor')
    referer = request.headers.get('Referer', 'Yok')
    path_info = request.full_path

    mesaj = (
        "🔔 *Yeni Ziyaretçi*\n\n"
        f"🌐 *IP:* `{ip}`\n"
        f"📱 *Cihaz/UA:* {ua}\n"
        f"🗣 *Dil:* {lang}\n"
        f"🔗 *Referer:* {referer}\n"
        f"📄 *Path:* `{path_info}`\n"
    )

    try:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": CHAT_ID,
                "text": mesaj,
                "parse_mode": "Markdown",
                "disable_web_page_preview": True,
            },
            timeout=5,
        )
    except Exception as e:
        print(f"Telegram gönderim hatası: {e}")

    return "OK", 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
