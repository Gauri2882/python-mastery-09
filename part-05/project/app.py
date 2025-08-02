""" Project: Portfolio Website Backend """

from flask import Flask, render_template, request
import json

app = Flask(__name__)

def save_feedback(name, email, message):
    feedback = {"name": name, "email": email, "message": message}
    try:
        with open("feedback.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(feedback) 

    with open("feedback.json", "w") as file:
        json.dump(data, file, indent= 4)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/feedback")
def view_feedback():
    try:
        with open("feedback.json", "r") as file:
            feedbacks = json.load(file)
    except FileNotFoundError:
        feedbacks = []

    return render_template('feedback.html', feedbacks = feedbacks)

@app.route("/submit-feedback", methods = ['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # save the feedback
    save_feedback(name, email, message)
    return "Feedback submitted successfully!"

if __name__ == "__main__":
    app.run(debug = True)