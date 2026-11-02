
import os
import json
import urllib.request
import urllib.error
import ssl
from datetime import datetime

# Load credentials from local .env
with open(".env", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line and not line.startswith("#"):
            key, value = line.split("=", 1)
            os.environ[key] = value.strip()

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# Simulated plant sensor readings
plant_id = "PLANT_01"
temperature = 29.0
humidity = 65
soil_status = "DRY"

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

message = (
    "SMART PLANT MONITORING SYSTEM\n\n"
    f"Plant ID: {plant_id}\n"
    f"Temperature: {temperature:.1f} C\n"
    f"Humidity: {humidity}%\n"
    f"Soil Moisture: {soil_status}\n"
    f"Time: {timestamp}\n\n"
    "Reason: Soil moisture below threshold\n"
    "Status: TEST NOTIFICATION\n\n"
    "This message uses simulated sensor readings."
)

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

payload = json.dumps({
    "chat_id": CHAT_ID,
    "text": message
}).encode("utf-8")

request = urllib.request.Request(
    url,
    data=payload,
    headers={"Content-Type": "application/json"},
    method="POST"
)

try:
    with urllib.request.urlopen(
        request,
        context=ssl.create_default_context(),
        timeout=15
    ) as response:
        result = json.load(response)

    if result.get("ok"):
        print("SUCCESS: Telegram notification delivered!")
    else:
        print("FAILED: Telegram rejected the request.")

except urllib.error.HTTPError as error:
    print(f"FAILED: Telegram HTTP {error.code}")
except (urllib.error.URLError, TimeoutError) as error:
    print(f"FAILED: Network error ({type(error).__name__})")
