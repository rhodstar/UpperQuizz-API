from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {
        "username": "Rodrigo",
        "theme": "AdaIP",
        "image": "image.png"
    }
