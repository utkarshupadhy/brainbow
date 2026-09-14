from pathlib import Path
import joblib

QUESTIONS = [
    {"id": "q1", "text": "Has difficulty making eye contact been observed?"},
    {"id": "q2", "text": "Does the child show limited response when their name is called?"},
    {"id": "q3", "text": "Are there noticeable difficulties with social interaction?"},
    {"id": "q4", "text": "Does the child repeat movements, sounds, or phrases frequently?"},
    {"id": "q5", "text": "Are there strong preferences for routines or resistance to change?"},
    {"id": "q6", "text": "Are unusual sensory sensitivities observed?"},
    {"id": "q7", "text": "Are communication or language delays a concern?"},
    {"id": "q8", "text": "Does the child show unusually intense interests?"},
    {"id": "q9", "text": "Is imaginative or pretend play limited?"},
    {"id": "q10", "text": "Are peer relationships difficult to establish or maintain?"},
]

MODEL_PATH = Path("model.pkl")

def _baseline(answers):
    values = []
    for question in QUESTIONS:
        try:
            values.append(max(0, min(3, int(answers.get(question["id"], 0)))))
        except (TypeError, ValueError):
            values.append(0)

    total = sum(values)
    maximum = len(QUESTIONS) * 3
    percentage = round((total / maximum) * 100, 1)

    if percentage < 30:
        category = "Low preliminary indication"
        level = "low"
        guidance = "Few indicators were selected. Continue observing development and discuss any concerns with a professional."
    elif percentage < 60:
        category = "Moderate preliminary indication"
        level = "moderate"
        guidance = "Some indicators were selected. Consider discussing the observations with a pediatrician or developmental specialist."
    else:
        category = "Higher preliminary indication"
        level = "high"
        guidance = "Several indicators were selected. A qualified professional assessment is recommended for further evaluation."

    return {
        "score": total,
        "percentage": percentage,
        "category": category,
        "level": level,
        "guidance": guidance,
        "disclaimer": "This result is a preliminary screening signal and is not a diagnosis."
    }

def predict_risk(answers):
    # A trained model can be plugged in when model.pkl exists.
    # The baseline remains available so the application works out of the box.
    if MODEL_PATH.exists():
        try:
            model = joblib.load(MODEL_PATH)
            vector = [[int(answers.get(q["id"], 0)) for q in QUESTIONS]]
            prediction = model.predict(vector)[0]
            baseline = _baseline(answers)
            baseline["category"] = str(prediction)
            baseline["level"] = "moderate"
            return baseline
        except Exception:
            pass
    return _baseline(answers)
