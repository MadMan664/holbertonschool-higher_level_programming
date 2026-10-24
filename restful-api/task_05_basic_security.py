#!/usr/bin/python3
"""A Flask API with Basic authentication, JWT and role based access."""
import os

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token, get_jwt,
                                jwt_required)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.environ.get(
    "JWT_SECRET_KEY", "change-this-long-secret-key-before-any-real-use")

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"),
              "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"),
               "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """Check the Basic credentials, return the username when valid."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@auth.error_handler
def basic_auth_error(status=401):
    """Answer 401 when the Basic credentials are missing or wrong."""
    return jsonify({"error": "Unauthorized"}), 401


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """No token was sent."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """The token is malformed or its signature is wrong."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_data):
    """The token has expired."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_data):
    """The token has been revoked."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_data):
    """A fresh token is required."""
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protected by Basic authentication."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Return a JWT when the credentials are valid."""
    data = request.get_json(force=True, silent=True)
    if not isinstance(data, dict):
        data = {}
    username = data.get("username")
    password = data.get("password")
    user = users.get(username) if isinstance(username, str) else None
    if (user is None or not isinstance(password, str) or
            not check_password_hash(user["password"], password)):
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_access_token(identity=username,
                                additional_claims={"role": user["role"]})
    return jsonify({"access_token": token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Route protected by a JWT."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route reserved to the users whose role is admin."""
    if get_jwt().get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
