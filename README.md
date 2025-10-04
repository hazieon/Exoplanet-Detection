







ORIGINAL INCREDIBLE PUBLIC OPEN SOURCE PROJECT - 

# 🌌 Kepler Exoplanet Detection

**Live Demo →** [kepler-exoplanet-detection.onrender.com](https://kepler-exoplanet-detection.onrender.com)

> 🚀 Predict whether a candidate is a confirmed exoplanet using machine learning and Kepler mission data.

---

## 🧠 What’s This Project About?

This project uses data from NASA's Kepler mission to predict whether a planetary candidate is likely to be a real exoplanet. It combines astrophysical parameters, uncertainty margins, and a user-friendly UI to perform real-time predictions using a machine learning model trained on labeled exoplanet data.

> 🎯 **Model Accuracy:** Achieved **95.6%** accuracy on the validation dataset using a Random Forest Classifier and Neural Networks.

---


## 📽️ Preview

![App Preview](./Screenshot%202025-06-03%20233238.png)

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS (custom styling, Montserrat font)
- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, pandas, joblib
- **Deployment**: Render

---

## 📊 Input Parameters

Users input ~37 different astrophysical parameters, including:
- Orbital period, transit depth, and duration
- Stellar radius, surface gravity, and temperature
- Planetary radius and equilibrium temperature
- Signal-to-noise ratios and uncertainties

👉 Want to test quickly? Click the **"Use Demo"** button to auto-fill real Kepler data!

---

## 🔍 How It Works

1. A form captures the input features related to a planetary candidate.
2. Flask sends the data to the backend where the trained ML model processes it.
3. The prediction is returned instantly: **Confirmed Exoplanet** or **Not Confirmed**.

---

## 📦 Setup Instructions

```bash
git clone https://github.com/yourusername/kepler-exoplanet-detection.git
cd kepler-exoplanet-detection
pip install -r requirements.txt
python app.py
