from flask import Flask, render_template, request, jsonify
from app.database import init_db, save_screening, get_recent_screenings
from app.model import predict_risk, QUESTIONS

app = Flask(__name__)
app.config["SECRET_KEY"] = "brainbow-development-key"
init_db()

@app.route("/")
def index():
    return render_template("index.html", questions=QUESTIONS)

@app.post("/api/predict")
def predict():
    payload = request.get_json(silent=True) or {}
    answers = payload.get("answers", {})
    result = predict_risk(answers)
    save_screening(answers, result)
    return jsonify(result)

@app.get("/api/history")
def history():
    return jsonify(get_recent_screenings())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
