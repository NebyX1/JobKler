from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)


@app.route("/")
def home():
    jobs = load_jobs_from_db()
    return render_template('home.html', Jobs = jobs)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3500, debug=True)