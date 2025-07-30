import requests

city = input("Enter city name: ")
url = f"https://wttr.in/{city}?format=%t"

response = requests.get(url)
print(f"Current temp in {city}: {response.text.strip()}")

