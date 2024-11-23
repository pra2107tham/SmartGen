import requests
import json
import os
from dotenv import load_dotenv
from flask import Blueprint, request, jsonify
load_dotenv()
tinyurlapikey=os.getenv("TINYURL")


# Create a Blueprint for the API
shorten_url = Blueprint("shorten_url", __name__)

@shorten_url.route("/shorten-url", methods=["POST"])
def shorten_url_endpoint():
    data = request.json
    input_url = data["url"]
    print(input_url)
    url = f"https://api.tinyurl.com/create?api_token={tinyurlapikey}"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "url": input_url
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.json())
    if response.status_code == 200:
        return jsonify({"shortened_url" : response.json()["data"]["tiny_url"]})
    else:
        return jsonify({"error": "Failed to shorten URL"}), 500
