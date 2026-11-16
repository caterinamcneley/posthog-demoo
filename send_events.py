
import json
import os
import urllib.request

API_KEY = os.environ["POSTHOG_PROJECT_KEY"]
HOST = os.environ["POSTHOG_HOST"]

with open("fake_events.json") as file:
    events = json.load(file)

payload = json.dumps({
    "api_key": API_KEY,
    "batch": events
}).encode("utf-8")

request = urllib.request.Request(
    f"{HOST}/batch/",
    data=payload,
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urllib.request.urlopen(request) as response:
    print("Events sent:", response.status)
