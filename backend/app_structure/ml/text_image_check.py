import requests
import base64
from flask import Blueprint, request, jsonify

# Hugging Face API URL and Authorization Header
API_URL = "https://api-inference.huggingface.co/models/openai/clip-vit-base-patch32"
headers = {"Authorization": "Bearer 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"}

# Create a Blueprint for the API
text_image_check = Blueprint("text_image_check", __name__)

@text_image_check.route("/text-image-check", methods=["POST"])
def text_image_check_endpoint():
    try:
        data = request.json
        # Check if image is a URL
        if data["image_path"].startswith("http"):
            # Download the image from the URL
            response = requests.get(data["image_path"])
            if response.status_code == 200:
                img = response.content
            else:
                return jsonify({"error": "Failed to download image from URL."}), 400
        else:
            # Read from local image path
            with open(data["image_path"], "rb") as f:
                img = f.read()

        # Encode the image to base64
        payload = {
            "parameters": data["parameters"],
            "inputs": base64.b64encode(img).decode("utf-8")
        }

        # Send the request
        response = requests.post(API_URL, headers=headers, json=payload)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500
