from flask import Flask
from connect_insta import connect_insta
from user_operations import user_operations
from database import db 
from ml.text_image_check import text_image_check
from ml.shorten_url import shorten_url

# Initialize Flask app
app = Flask(__name__)



# Register the Instagram connection Blueprint
app.register_blueprint(connect_insta, url_prefix="/api/instagram")
app.register_blueprint(user_operations, url_prefix="/api/user")
app.register_blueprint(text_image_check, url_prefix="/api/ml")
app.register_blueprint(shorten_url, url_prefix="/api/ml")

if __name__ == '__main__':
    try:
        app.run(port=8000, debug=True)
    except Exception as e:
        print(f"Error starting Flask app: {e}")
