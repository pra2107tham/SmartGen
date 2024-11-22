from flask import Flask
from connect_insta import connect_insta
from user_operations import user_operations
from database import db 

# Initialize Flask app
app = Flask(__name__)



# Register the Instagram connection Blueprint
app.register_blueprint(connect_insta, url_prefix="/api/instagram")
app.register_blueprint(user_operations, url_prefix="/api/user")

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting Flask app: {e}")
