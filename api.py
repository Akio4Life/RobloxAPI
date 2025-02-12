from flask import Flask, request
import requests
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route("/ban", methods=["POST"])
def ban_player():
    app.logger.debug("Ban route was hit")
    data = request.json
    user_id = data.get("user_id")
    
    # Your ban logic
    return {"message": f"Banned user {user_id}"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
