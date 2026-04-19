import requests
import time

# Добавляем случайное число в конец ссылки, чтобы сбросить кэш
timestamp = int(time.time())
url = f"https://raw.githubusercontent.com/Xtwo-oss/test-repository/main/"

response = requests.get(f"{url}{input('enter file name:')}?nocache={timestamp}")
# Теперь ты получишь самую свежую версию без задержек!
if response.status_code == 200:
    print(response.text)
    exec(response.text)
else:
    print("Не удалось загрузить файл")