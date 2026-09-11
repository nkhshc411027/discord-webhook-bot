import os
import requests

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]

message = """<@&1541830487532900533> ついてきて

ねねねねねねね
ねねねねねねね
ねねねねねねねね(ねね！)
ねねねねねね(ねね！)
ねねねねね(ね！)
ね"""

response = requests.post(
    WEBHOOK_URL,
    json={
        "content": message,
        "allowed_mentions": {
            "roles": ["1541830487532900533"]
        }
    }
)

print("Status:", response.status_code)
print(response.text)
