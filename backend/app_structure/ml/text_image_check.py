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
    """
    Check text-image consistency using Hugging Face's CLIP model.
    """
    try:
        data = request.json
        image_path = data.get("image_path")
        parameters = data.get("parameters")

        if not image_path or not parameters:
            return jsonify({"error": "Both 'image_path' and 'parameters' are required"}), 400

        if "candidate_labels" not in parameters:
            return jsonify({"error": "'candidate_labels' is required in 'parameters'"}), 400

        # Check if image is a URL
        if image_path.startswith("http"):
            # Download the image from the URL
            response = requests.get(image_path)
            if response.status_code == 200:
                img = response.content
            else:
                return jsonify({"error": "Failed to download image from URL."}), 400
        else:
            # Read from local image path
            with open(image_path, "rb") as f:
                img = f.read()

        # Encode the image to base64
        encoded_image = base64.b64encode(img).decode("utf-8")

        # Prepare payload for Hugging Face API
        payload = {
            "inputs": {
                "image": encoded_image,
                "text": parameters["candidate_labels"][0]
            }
        }

        # Send the request to Hugging Face API
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            return jsonify(response.json())
        elif response.status_code == 401:
            return jsonify({"error": "Invalid authorization token."}), 401
        else:
            return jsonify({"error": f"Failed to analyze image-text consistency: {response.text}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
