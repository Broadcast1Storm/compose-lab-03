from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Task2: Profiles working"
app.run(host="0.0.0.0", port=6000)
