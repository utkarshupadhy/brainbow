from pathlib import Path
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

DATA_PATH = Path("data/sample_screening_data.csv")
MODEL_PATH = Path("model.pkl")

df = pd.read_csv(DATA_PATH)
feature_columns = [column for column in df.columns if column.startswith("q")]
X = df[feature_columns]
y = df["label"]

model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")
model.fit(X, y)
joblib.dump(model, MODEL_PATH)
print(f"Model saved to {MODEL_PATH.resolve()}")
