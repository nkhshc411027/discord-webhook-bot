import requests

WEBHOOK_URL = "ここにDiscordのWebhook URLを入れます"

message = """ついてきて

ねねねねねねね
ねねねねねねね
ねねねねねねねね(ねね！)
ねねねねねね(ね！)
ねねねねね(ね！)
ね"""

data = {
    "content": message
}

response = requests.post(WEBHOOK_URL, json=data)

print(response.status_code)
