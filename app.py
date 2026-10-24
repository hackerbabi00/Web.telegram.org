import os
from flask import Flask, redirect

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect('https://iplogger.com/2PMDK5', code=301)

if __name__ == '__main__':
    # Temel nokta: host 0.0.0.0 olmalı ve port PORT ortam değişkeninden okunmalı
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
