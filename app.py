from flask import render_template
from flask import Flask, jsonify, request, redirect, url_for
from flask_socketio import SocketIO
import threading
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__,template_folder='templates')
app.jinja_env.cache = {}

cred = credentials.Certificate(
    "portfolioshrinivasaprasada-firebase-adminsdk-qlcxs-77577b3327.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.route('/')
def index():
    achievements = db.collection('achievements').get()
    data = db.collection('data').document("information").get()
    homepage = db.collection('homepage').document("homepage").get()
    projects = db.collection('projects').get()
    skills = db.collection('skills').get()
    social = db.collection('social').get()
    return render_template("index.html", data=data, achievements=achievements, homepage=homepage, projects=projects,
                           skills=skills, social=social)


@app.route("/forms", methods=["POST"])
def get_form():
    email = request.form.get("email")
    title = request.form.get("title")
    des = request.form.get("des")
    db.collection("connection").add({
        "email": email,
        "title": title,
        "des": des
    })
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
