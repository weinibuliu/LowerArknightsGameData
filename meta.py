# Get Timestamp and read config.json

import time
import json
import subprocess
from pathlib import Path

timestamp = int(time.time())
subprocess.check_call(f'echo timestamp={timestamp} >> "$GITHUB_ENV"', shell=True)
print(f"timestamp: {timestamp}")

with open(f"{Path.cwd()}/config.json", "r", encoding="utf-8") as c:
    configs: dict[str] = json.load(c)

for config in configs.items():
    name = config[0]
    value = config[1]
    subprocess.check_call(f'echo {name}={value} >> "$GITHUB_ENV"', shell=True)
    print(f"{name} = {value}")
