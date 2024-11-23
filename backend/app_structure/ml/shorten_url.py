import requests
import json
from flask import Blueprint, request, jsonify

# Create a Blueprint for the API
shorten_url = Blueprint("shorten_url", __name__)

@shorten_url.route("/shorten-url", methods=["POST"])
def shorten_url_endpoint():
    img_url = request.json.get("img_url")
    url = "https://spoo.me"
    payload = {
        "url": img_url
    }
    headers = {
        "Accept": "application/json"
    }
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        res = response.json()
        return jsonify({"short_url": res.get("short_url")})
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return jsonify({"error": "Failed to shorten URL"}), response.status_code