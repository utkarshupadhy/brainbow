## Live Demo

[Brainbow Live Demo]
(https://brainbow-live-demo.hatchable.site)


# Brainbow — Early Autism Screening System

A machine-learning prototype that analyzes behavioral questionnaire responses and estimates a preliminary risk category.

> **Important:** This is an educational screening aid, not a diagnostic tool. It does not replace a qualified clinician or formal assessment.

## Features
- Flask web interface
- Questionnaire-based input
- Rule-based baseline model that works immediately
- Optional scikit-learn training pipeline
- Risk score and category
- SQLite storage for screening records
- CSV sample dataset
- Responsive interface

## Project structure
```text
Brainbow/
├── app.py
├── train_model.py
├── requirements.txt
├── .env.example
├── data/sample_screening_data.csv
├── app/
│   ├── model.py
│   └── database.py
├── templates/index.html
└── static/style.css
```

## Run locally

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Optional model training

```bash
python train_model.py
```

The training script creates `model.pkl`. If it is not present, Brainbow uses a transparent baseline scoring model.

## Input interpretation
Each question is scored from 0 to 3:
- 0 = Never / no concern
- 1 = Sometimes
- 2 = Often
- 3 = Very often

The output is categorized as:
- Low preliminary indication
- Moderate preliminary indication
- Higher preliminary indication

The score is only a preliminary signal and must not be interpreted as a diagnosis.
