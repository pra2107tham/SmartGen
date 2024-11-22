from flask import Blueprint, request, jsonify
import requests
from datetime import datetime, timedelta
from database import db 

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

@connect_insta.route('/connection', methods=['POST'])
def instagram_connection():
    """
    Handle Instagram connection, store user and media data in the database.
    """
    data = request.json
    code = data.get("code")
    email = data.get("email")

    if not code:
        return jsonify({"error": "Authorization code is required"}), 400

    # Step 1: Get short-lived token
    oauth_response = get_short_lived_token(code)
    if not oauth_response:
        return jsonify({"error": "Failed to fetch short-lived token"}), 500

    short_lived_token = oauth_response.get("access_token")
    user_id = oauth_response.get("user_id")

    if not short_lived_token or not user_id:
        return jsonify({"error": "Invalid response from OAuth"}), 400

    # Step 2: Exchange for a long-lived token
    token_response = exchange_for_long_lived_token(short_lived_token)
    if not token_response:
        return jsonify({"error": "Failed to exchange for long-lived token"}), 500

    long_lived_token = token_response["access_token"]
    expiry_in_seconds = token_response.get("expires_in", 86400)
    token_expiry = datetime.utcnow() + timedelta(seconds=expiry_in_seconds)

    # Step 3: Fetch user details
    user_details = fetch_user_details(long_lived_token)
    if not user_details:
        return jsonify({"error": "Failed to fetch user details"}), 500

    # Step 4: Fetch and store media details
    media_data = fetch_media_details(long_lived_token)

    # Store media details in the "media" collection
    media_ids = []
    for media in media_data:
        media_id = media.get("id")
        if media_id:
            db.media.update_one(
                {"media_id": media_id}, {"$set": media}, upsert=True
            )
            media_ids.append(media_id)

    # Insert user data into MongoDB
    user_data = {
        "instagram_id": user_id,
        "username": user_details.get("username"),
        "access_token": long_lived_token,
        "token_expiry": token_expiry,
        "instagram_connected": True,
        "media": media_ids,  # Store only media IDs in the user document
        "created_at": datetime.now(),
        "biography": user_details.get("biography"),
        "media_count": user_details.get("media_count"),
        "account_type": user_details.get("account_type"),
    }
    db.users.update_one(
        {"email": email}, {"$set": user_data}, upsert=True
    )

    return jsonify({"message": "Instagram connection successful", "media_ids": media_ids, "user_data": user_data}), 200



@connect_insta.route('/connected-users', methods=['GET'])
def get_connected_users():
    connected_users = list(db.users.find({"instagram_connected": True}, {"_id": 0}))
    return jsonify({"connected_users": connected_users}), 200