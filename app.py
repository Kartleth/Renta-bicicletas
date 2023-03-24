from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for, abort

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")
    
if __name__ == '__main__':
    app.run(debug=True)