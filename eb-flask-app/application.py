import os

from flask import Flask, jsonify

application = Flask(__name__)


@application.route("/")
def home():
    env = os.environ.get("APP_ENV", "development")
    return f"<h1>Hello from Elastic Beanstalk!</h1><p>Environment: {env}</p>"


@application.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    # Debug is off unless explicitly enabled, so it is never on in production
    application.run(debug=os.environ.get("FLASK_DEBUG") == "1")