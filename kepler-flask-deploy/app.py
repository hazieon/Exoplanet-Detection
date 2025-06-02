from flask import Flask, request, render_template
import numpy as np
from tensorflow.keras.models import load_model
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load model and scaler
model = load_model("kepler-flask-deploy/model/exoplanet_model.keras")
scaler = joblib.load("kepler-flask-deploy/model/scaler.pkl")
# Home route
@app.route("/")
def index():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract inputs from form
        features = [float(request.form[f]) for f in request.form]
        features_np = np.array([features])  # Make it 2D

        # Preprocess with scaler
        features_scaled = scaler.transform(features_np)

        # Predict
        prediction = model.predict(features_scaled)[0][0]
        result = "🌍 Exoplanet Detected!" if prediction > 0.5 else "❌ Not an Exoplanet."

        return render_template("index.html", prediction_text=result)
    except Exception as e:
        return render_template("index.html", prediction_text=f"⚠️ Error: {str(e)}")

# Run app
if __name__ == "__main__":
    app.run(debug=True)
