from datetime import datetime

import requests


city = input("Enter city name: ")
url = f"https://wttr.in/{city}?format=%t"

response = requests.get(url)
print(f"Current temp in {city}: {response.text.strip()}")

timestamp = datetime.now().isoformat(timespec="seconds")
log_line = f"{timestamp} — {city}: {response.text.strip()}\n"

with open("weather_log.txt", "a") as f:
    f.write(log_line)

