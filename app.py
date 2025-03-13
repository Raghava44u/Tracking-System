from flask import Flask, render_template, request, session, redirect, url_for
import time

app = Flask(__name__)
app.secret_key = "secret"

# Sample questions
questions = [
    {"question": "What is 5 + 3?", "options": ["6", "7", "8", "9"], "answer": "8"},
    {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    {"question": "Solve: 12 × 2 - 4", "options": ["20", "22", "24", "26"], "answer": "20"},
    {"question": "What is 9 ÷ 3?", "options": ["2", "3", "4", "5"], "answer": "3"},
    {"question": "Solve: 15 × 4 + 3", "options": ["63", "60", "64", "58"], "answer": "63"},
]

@app.route("/")
def index():
    session["current_q"] = 0
    session["responses"] = []
    session["start_time"] = time.time()

    if "login_times" not in session:
        session["login_times"] = []
    
    session["login_start"] = time.time()

    return redirect(url_for("quiz"))

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if session["current_q"] >= len(questions):
        return redirect(url_for("visualization"))

    if request.method == "POST":
        user_answer = request.form.get("answer")
        end_time = time.time()
        time_taken = round(end_time - session["start_time"], 2)

        session["responses"].append({
            "question": questions[session["current_q"]]["question"],
            "correct": user_answer == questions[session["current_q"]]["answer"],
            "time": time_taken
        })

        session["current_q"] += 1
        session["start_time"] = time.time() 
    if session["current_q"] < len(questions):
        return render_template("index.html", 
                               question=questions[session["current_q"]], 
                               q_num=session["current_q"] + 1)

    return redirect(url_for("visualization"))

@app.route("/logout")
def logout():
    if "login_start" in session:
        login_end = time.time()
        login_duration = round(login_end - session["login_start"], 2)

        session["login_times"].append({
            "timestamp": int(session["login_start"]),
            "duration": login_duration
        })

        session.pop("login_start") 

    return redirect(url_for("visualization"))

@app.route("/visualization")
def visualization():
    login_data = session.get("login_times", [])
    return render_template("visualization.html", 
                           results=session.get("responses", []), 
                           login_data=login_data)

if __name__ == "__main__":
    app.run(debug=True)
