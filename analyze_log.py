from datetime import datetime
from statistics import mean
import re

def parse_line(line):
    # Example line: 2025-07-30T15:28:09 — NYC: +33°C
    timestamp_str, rest = line.split(" — ")
    city, temp_part = rest.split(": ")
    temp_c = int(re.findall(r"-?\d+", temp_part)[0])   # grabs 33 from +33°C
    ts = datetime.fromisoformat(timestamp_str)
    return ts.date(), city, temp_c

dates = {}
with open("weather_log.txt") as f:
    for line in f:
        day, city, temp = parse_line(line.strip())
        dates.setdefault(day, []).append(temp)

for day, temps in sorted(dates.items()):
    print(f"{day}: avg {mean(temps):.1f}°C from {len(temps)} readings")
