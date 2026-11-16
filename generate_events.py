
import json
import random
from datetime import datetime, timezone

events = [
    "user_signed_up",
    "onboarding_started",
    "onboarding_completed",
    "feature_used",
    "subscription_started"
]

fake_data = []

for i in range(100):
    fake_data.append({
        "event": random.choice(events),
        "distinct_id": f"demo_user_{random.randint(1, 30)}",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "properties": {
            "plan": random.choice(["free", "pro", "enterprise"]),
            "device": random.choice(["desktop", "mobile"]),
            "is_demo": True
        }
    })

with open("fake_events.json", "w") as file:
    json.dump(fake_data, file, indent=2)

print("Generated 100 fake PostHog events!")
