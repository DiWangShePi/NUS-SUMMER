#!/usr/bin/env python

import time
from flask import Flask, render_template, request
import os

app = Flask(__name__)

FLAG = os.environ["SECRET"]
assert " " not in FLAG
TINY_TIME = 6.114514 * 10 ** -44

users = {
    "admin": {"password": "123456"},
}

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST","GET"])
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    if username not in users:
        return "Invalid username or password!"

    user = users[username]
    if user["password"] != password:
        return "Invalid username or password!"

    return "Login successful!"

@app.route("/<secret>")
def check_secret(secret):
    if not secret:
        return "WAKUWAKU!"
    if len(secret) != len(FLAG):
        return "WAKUWAKU!"
    for a, b in zip(secret, FLAG):
        if a == " ":
            continue
        elif a != b:
            return "WRONG!"
        else:
            time.sleep(TINY_TIME)
    if " " in secret:
        return "WRONG!"
    return "CORRECT!"

if __name__ == "__main__":
    app.run()