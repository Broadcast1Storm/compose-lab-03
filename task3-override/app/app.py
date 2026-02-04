import os
import sys
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return f"Mode={os.getenv('MODE')} Debug={'--debug' in sys.argv}"
app.run(host="0.0.0.0", port=7000)
