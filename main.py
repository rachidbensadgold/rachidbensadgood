import time
import requests

TOKEN = "8628469175:AAHyisDg2Umf4FKw8AqBf1VUqchfE5j4k50"  #[span_0](start_span)[span_0](end_span)
CHAT_ID = "7461058423"  #[span_1](start_span)[span_1](end_span)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload, timeout=5)
        print("تم إرسال سعر الذهب إلى تيليجرام بنجاح.")
    except Exception as e:
        print("خطأ في إرسال الميساج:", e)

print("بدأ اختبار إرسال سعر الافتتاح للذهب كل دقيقة...")

last_sent_candle_time = None

while True:
    try:
        url = "https://api.binance.com/api/v3/klines?symbol=PAXGUSDT&interval=1m&limit=1"
        response = requests.get(url, timeout=5)
        candle = response.json()[0]
        
        open_time = candle[0]   
        open_price = candle[1]  
        
        if open_time != last_sent_candle_time:
            message = f"🟡 شمعة دقيقة جديدة للذهب (Gold):\nسعر الافتتاح (Open): {open_price}"
            send_telegram_message(message)
            last_sent_candle_time = open_time

    except Exception as e:
        print("حدث خطأ أثناء فحص شمعة الذهب:", e)

    time.sleep(10)
