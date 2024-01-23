#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

user_profiles = {
    'john_doe': {'name': 'John Doe', 'age': 25, 'email': 'john@example.com'},
    'jane_smith': {'name': 'Jane Smith', 'age': 30, 'email': 'jane@example.com'},
}

# append to app/app.py
@app.route('/')
def index():
    return '<h1>Using flask to develop web applications</h1>'

@app.route('/<string:username>')
def user(username):
    if username in user_profiles:
        profile = user_profiles[username]
        return f'<h2>Profile for {profile["name"]}</h2><p>Age: {profile["age"]}</p><p>Email: {profile["email"]}</p>'
    else:
        return f'<h2>User {username} not found</h2>'
    
if __name__ == '__main__':
    app.run(debug=True)
