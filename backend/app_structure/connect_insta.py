from flask import Blueprint, request, jsonify
import requests
from datetime import datetime, timedelta
from database import db 
import re  # Import the regex library


# Create Blueprint for Instagram connection
connect_insta = Blueprint('connect_insta', __name__)

# Instagram API Credentials
INSTAGRAM_CLIENT_ID = "1071555971386941"
INSTAGRAM_CLIENT_SECRET = "72ffd47016434122b6f69a040e62b690"
INSTAGRAM_REDIRECT_URI = "https://127.0.0.1/dashboard"

API_URL = "https://api-inference.huggingface.co/models/openai/clip-vit-base-patch32"
HEADERS = {"Authorization": f"Bearer YOUR_HUGGINGFACE_API_KEY"}

def get_short_lived_token(code):
    """
    Exchange authorization code for a short-lived access token.
    """
    url = "https://api.instagram.com/oauth/access_token"
    data = {
        "client_id": INSTAGRAM_CLIENT_ID,
        "client_secret": INSTAGRAM_CLIENT_SECRET,
        "grant_type": "authorization_code",
        "redirect_uri": INSTAGRAM_REDIRECT_URI,
        "code": code,
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching short-lived token: {response.status_code} {response.text}")
        return None


def exchange_for_long_lived_token(short_lived_token):
    """
    Exchange a short-lived token for a long-lived token.
    """
    url = "https://graph.instagram.com/access_token"
    params = {
        "grant_type": "ig_exchange_token",
        "client_secret": INSTAGRAM_CLIENT_SECRET,
        "access_token": short_lived_token,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching long-lived token: {response.status_code} {response.text}")
        return None


def fetch_user_details(access_token):
    """
    Fetch user details from Instagram Graph API.
    """
    url = "https://graph.instagram.com/me"
    params = {
        "fields": "id,username,biography,media_count,account_type",
        "access_token": access_token,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching user details: {response.status_code} {response.text}")
        return None


def fetch_media_details(access_token):
    """
    Fetch media details from Instagram Graph API.
    """
    url = "https://graph.instagram.com/me/media"
    params = {
        "fields": "id,caption,media_type,media_url,like_count,comments_count",
        "access_token": access_token,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print(f"Error fetching media details: {response.status_code} {response.text}")
        return None



from flask import Blueprint, request, jsonify
import requests
from datetime import datetime
import re

API_URL = "https://api-inference.huggingface.co/models/openai/clip-vit-base-patch32"
HEADERS = {"Authorization": "Bearer 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"}

# Create Blueprint for Instagram connection
connect_insta = Blueprint('connect_insta', __name__)

# Instagram API Credentials
INSTAGRAM_CLIENT_ID = "1071555971386941"
INSTAGRAM_CLIENT_SECRET = "72ffd47016434122b6f69a040e62b690"
INSTAGRAM_REDIRECT_URI = "https://127.0.0.1/dashboard"

def get_short_lived_token(code):
    """
    Exchange authorization code for a short-lived access token.
    """
    url = "https://api.instagram.com/oauth/access_token"
    data = {
        "client_id": INSTAGRAM_CLIENT_ID,
        "client_secret": INSTAGRAM_CLIENT_SECRET,
        "grant_type": "authorization_code",
        "redirect_uri": INSTAGRAM_REDIRECT_URI,
        "code": code,
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching short-lived token: {response.status_code} {response.text}")
        return None


def exchange_for_long_lived_token(short_lived_token):
    """
    Exchange a short-lived token for a long-lived token.
    """
    url = "https://graph.instagram.com/access_token"
    params = {
        "grant_type": "ig_exchange_token",
        "client_secret": INSTAGRAM_CLIENT_SECRET,
        "access_token": short_lived_token,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching long-lived token: {response.status_code} {response.text}")
        return None


def fetch_user_details(access_token):
    """
    Fetch user details from Instagram Graph API.
    """
    url = "https://graph.instagram.com/me"
    params = {
        "fields": "id,username,biography,media_count,account_type",
        "access_token": access_token,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching user details: {response.status_code} {response.text}")
        return None


def fetch_media_details(access_token):
    """
    Fetch media details from Instagram Graph API.
    """
    url = "https://graph.instagram.com/me/media"
    params = {
        "fields": "id,caption,media_type,media_url,like_count,comments_count",
        "access_token": access_token,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print(f"Error fetching media details: {response.status_code} {response.text}")
        return None

@connect_insta.route("/connection", methods=["POST"])
def connect_to_insta():
    """
    Connect to Instagram, fetch media, analyze text-image consistency, and store results.
    """
    try:
        # Get the input JSON data (including code and email)
        data = request.json
        code = data.get("code")  # Extract the code
        email = data.get("email")  # Extract the email

        # Validate code and email
        if not code or not email:
            return jsonify({"error": "Both code and email are required"}), 400

        # Exchange the authorization code for a short-lived token
        token_response = get_short_lived_token(code)
        if not token_response:
            return jsonify({"error": "Failed to exchange code for token"}), 500

        access_token = token_response.get("access_token")
        instagram_id = token_response.get("user_id")

        if not access_token:
            return jsonify({"error": "Failed to obtain access token"}), 500

        # Fetch user details using the access token
        user_data = fetch_user_details(access_token)
        if not user_data:
            return jsonify({"error": "Failed to fetch user details from Instagram"}), 500

        # Optional: Store or use the email for further purposes (e.g., associating with the user in your system)

        # Fetch the user's media
        media_data = fetch_media_details(access_token)
        if not media_data:
            return jsonify({"error": "Failed to fetch media details"}), 500

        media_ids = []

        # Process each media item
        for media in media_data:
            media_id = media.get("id")
            caption = media.get("caption", "")
            media_url = media.get("media_url")

            # Extract hashtags from the caption
            hashtags = re.findall(r"#\w+", caption)

            # Analyze text-image consistency using Hugging Face
            payload = {
                "inputs": {
                    "image": media_url,  # Provide the media URL
                    "text": caption  # Provide the caption text
                }
            }
            clip_response = requests.post(API_URL, headers=HEADERS, json=payload)

            if clip_response.status_code != 200:
                print(f"Skipping media {media_id} due to failed analysis: {clip_response.text}")
                continue

            clip_result = clip_response.json()
            score = clip_result.get("score", 0)  # Default to 0 if no score

            # Discard media if score is below threshold
            if score < 0.35:
                print(f"Discarding media {media_id} due to low consistency score: {score}")
                continue

            if media_id:
                media_doc = {
                    "media_id": media_id,
                    "caption": caption,
                    "hashtags": hashtags,
                    "media_type": media.get("media_type"),
                    "media_url": media_url,
                    "like_count": media.get("like_count"),
                    "comments_count": media.get("comments_count"),
                    "email": email,  # Use the email provided in the input
                    "created_at": datetime.now()
                }

                # Insert or update media in database (replace `db` with your DB connection)
                db.media.update_one(
                    {"media_id": media_id}, {"$set": media_doc}, upsert=True
                )
                media_ids.append(media_id)

        return jsonify({
            "media_ids": media_ids,
            "message": "Instagram connection successful",
            "email": email,  # Include email in the response
            "user_data": user_data,
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@connect_insta.route('/connected-users', methods=['GET'])
def get_connected_users():
    connected_users = list(db.users.find({"instagram_connected": True}, {"_id": 0}))
    return jsonify({"connected_users": connected_users}), 200