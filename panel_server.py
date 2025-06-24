from flask import Flask, render_template, request
import datetime
import requests

app = Flask(__name__)

BOT_TOKEN = '8013913146:AAEXuyH7lUrkv1YMCrLQv_CRsaRwE7wMBks'
CHAT_ID = '6667215984'

def send_telegram_alert(ip, user_agent):
    message = f"""🚨 Sahte bağlantıya tıklama algılandı!

🕒 Zaman: {datetime.datetime.now()}
🌐 IP: {ip}
📱 Tarayıcı: {user_agent}
"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"[!] Telegram hatası: {e}")

@app.route('/')
def fake_admin_panel():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    send_telegram_alert(ip, user_agent)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)