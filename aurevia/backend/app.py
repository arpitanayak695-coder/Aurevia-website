from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app)

@app.route('/api/contact', methods=['POST'])
def handle_contact():
    try:
        data = request.get_json()

        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone', 'N/A')
        property_name = data.get('property', 'General enquiry')
        message = data.get('message')

        if not name or not email or not message:
            return jsonify({
                "success": False,
                "message": "Please fill in all required fields (Name, Email, Message)."
            }), 400

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n" + "="*50)
        print(f"📩 NEW INQUIRY RECEIVED [{timestamp}]")
        print("="*50)
        print(f"Name     : {name}")
        print(f"Email    : {email}")
        print(f"Phone    : {phone}")
        print(f"Property : {property_name}")
        print(f"Message  : {message}")
        print("="*50 + "\n")


        return jsonify({
            "success": True,
            "message": "Thank you. Your inquiry has been sent successfully!"
        }), 200

    except Exception as e:
        print(f"Error handling inquiry: {e}")
        return jsonify({
            "success": False,
            "message": "An internal server error occurred. Please try again later."
        }), 500

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    print(f"AUREVIA Python Backend is running on http://localhost:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)