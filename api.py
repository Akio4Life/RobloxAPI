import os
from flask import Flask, request
import requests

app = Flask(__name__)

ROBLOX_API_KEY = "dckPx800Bk+fdCuHGnfkphpH8kvdTcNc5tg4hjpToYLfFIuvZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNkluTnBaeTB5TURJeExUQTNMVEV6VkRFNE9qVXhPalE1V2lJc0luUjVjQ0k2SWtwWFZDSjkuZXlKaVlYTmxRWEJwUzJWNUlqb2laR05yVUhnNE1EQkNheXRtWkVOMVNFZHVabXR3YUhCSU9HdDJaRlJqVG1NMWRHYzBhR3B3Vkc5WlRHWkdTWFYySWl3aWIzZHVaWEpKWkNJNklqTTBOVGsyT0RFMUlpd2lZWFZrSWpvaVVtOWliRzk0U1c1MFpYSnVZV3dpTENKcGMzTWlPaUpEYkc5MVpFRjFkR2hsYm5ScFkyRjBhVzl1VTJWeWRtbGpaU0lzSW1WNGNDSTZNVGN6T1RNek9UazFNaXdpYVdGMElqb3hOek01TXpNMk16VXlMQ0p1WW1ZaU9qRTNNemt6TXpZek5USjkuRUlNb2ZqakJ0Tmx0OXJZeWNWTjlzenNHMXRxMV96OFZMNl9WUFNFWEFoTElLQ3lDSm1qc2hDckJudG9LOE9rUkhHODhUY3U5cTlLNnVad3NOeUI2LVN6bzZJQTJFZ190VFBqZ0gwc3ZuQkFrYUdueUFGalZ6RHdpRV9mWlhhSGhuZE9NdzVjSUx0eC1mREZMRHlWOTl2bUtaQjgwdksxTDIwOEc5MVVTMlpJM2FLSU1DZjVhTWJxSXNUenMtbk0zSzhqdEZoa3ZVa1cxNXVQalROVWs3ZVdibkptN2hzZmwtUUJxc0ZybHdfcTF3ejUwazdMVHZVX0dUNVMxaU9QcHlTUVNSY01NMzJROHgwYkcxRWpYRXRPeXlUZndzVzhXZEExTFlRWUwtOGNQRElicjVMd1lLeTd0WkIwOGVtNVFzY1hBaFI3NGNLSVd3SHlvLXFOamd3"
GAME_ID = "116926066978250"

@app.route("/ban", methods=["POST"])
def ban_player():
    data = request.json
    user_id = data.get("user_id")

    # Send request to Roblox DataStore
    headers = {"x-api-key": ROBLOX_API_KEY, "Content-Type": "application/json"}
    response = requests.post(
        f"https://apis.roblox.com/datastores/v1/universes/{GAME_ID}/standard-datastores/BannedPlayers/entries",
        json={"entryKey": str(user_id), "entryValue": "banned"},
        headers=headers
    )
    return response.json(), response.status_code

if __name__ == "__main__":
    port = os.getenv('PORT', 5000)  # Get the PORT from environment variable
    app.run(host='0.0.0.0', port=port)
