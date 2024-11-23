from flask import Blueprint, request, jsonify
import requests
from datetime import datetime, timedelta
from pymongo import MongoClient
from database import db
from bson import ObjectId
from connect_insta import fetch_media_details

# Create Blueprint for Instagram connection
user_operations = Blueprint('user_operations', __name__)

# Instagram API Credentials
INSTAGRAM_CLIENT_ID = "1071555971386941"
INSTAGRAM_CLIENT_SECRET = "72ffd47016434122b6f69a040e62b690"
INSTAGRAM_REDIRECT_URI = "https://127.0.0.1/dashboard"

@user_operations.route("/fetch-user-media", methods=["POST"])
def fetch_new_user_media():
    user_id = request.json.get("user_id")
    try:
        user_id = ObjectId(user_id)
    except Exception as e:
        return jsonify({"error": "Invalid user_id format"}), 400

    # Fetch the user from the database
    user = db.users.find_one({"_id": user_id})
    if not user:
        return jsonify({"error": "User not found"}), 404

    access_token = user.get("access_token")
    if not access_token:
        return jsonify({"error": "Access token not found for user"}), 400

    # Fetch media details using Instagram API
    media_data = fetch_media_details(access_token)
    if not media_data:
        return jsonify({"error": "Failed to fetch media details"}), 500

    media_ids = set()  # Use a set to automatically handle duplicates

    # Update or insert each media item into the media collection
    for media in media_data:
        media_id = media.get("id")
        if media_id not in db.users.find_one({"_id": user_id}).get("media"):
            # Update the media document if it exists, or insert it
            db.media.update_one({"media_id": media_id}, {"$set": media}, upsert=True)
            media_ids.add(media_id)  # Add to the set to ensure unique IDs

    # Fetch existing media IDs from the user's record, if any
    existing_media_ids = set(user.get("media", []))

    # Merge the new media IDs with the existing ones and remove duplicates
    all_media_ids = list(existing_media_ids.union(media_ids))

    # Update the user's media field with the merged list of media IDs
    db.users.update_one({"_id": user_id}, {"$set": {"media": all_media_ids}})

    return jsonify({"message": "Media updated successfully", "media_ids": all_media_ids}), 200


@user_operations.route("/update-media-item", methods=["POST"])
def update_media_item():
    data = request.json

    # Extract the user_id and media_id from the input
    user_id_str = data.get("user_id").get("$oid")  # Safely access the nested structure
    media_id = data.get("media_id")

    # Validate the user_id format
    try:
        user_id = ObjectId(user_id_str)
    except Exception as e:
        return jsonify({"error": "Invalid user_id format"}), 400

    # Fetch the user from the database
    user = db.users.find_one({"_id": user_id})
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Fetch the media item from the database
    user_media = db.media.find_one({"media_id": media_id})
    if not user_media:
        return jsonify({"error": "Media item not found"}), 404

    # Prepare the fields to update
    edits = {
        "media_id": media_id,
        "caption": data.get("caption"),
        "comments_count": data.get("comments_count"),
        # "id": data.get("id"),
        "like_count": data.get("like_count"),
        "media_type": data.get("media_type"),
        "media_url": data.get("media_url"),
    }

    # Remove `None` values from the edits dictionary
    updates = {key: value for key, value in edits.items() if value is not None}

    # Update the media item in the database
    db.media.update_one({"media_id": media_id}, {"$set": updates})

    return jsonify({"message": "Media updated successfully", "updated_fields": updates}), 200
