# 🌌 K2 Exoplanet Detection

> 🚀 Predict whether a candidate is a confirmed exoplanet using machine learning and K2 NASA mission data.

# EXPLORE FOR YOURSELF:
Take a deep dive into our A.I model and try out the model on new data to classify NEW Exoplanets
[Playground](https://colab.research.google.com/drive/1KqPKqPoVj_znV-4Hble0yDQ4oLJCee63?usp=sharing)

---

## 🧠 What’s This Project About?

This project uses data from NASA's **K2** mission to classify planetary candidates and predict whether they are likely to be a real exoplanet. 
It combines astrophysical parameters, uncertainty margins using a machine learning model trained on REAL NASA labeled exoplanet data.

> 🎯 **Model Performance metrics:**
> Achieved **96%** accuracy on the validation dataset using a Random Forest Classifier
> Achieved **92.5%** with a Neural Network model

> Visualised through figures of Accuracy, Loss, Confusion Matrix
> Class weights prevent the model from overtraining on majority or ignoring the minority class
> Predict the planetary status of unseen planets from the [Playground](https://colab.research.google.com/drive/1KqPKqPoVj_znV-4Hble0yDQ4oLJCee63?usp=sharing) or via the **front end Exoplanet UI**

---


## 📽️ Preview

![App Preview](./Screenshot%202025-06-03%20233238.png)

---

## 📊 Input Parameters

The neural network receives 46 numerical features describing stars, planets, and their orbital systems, including:

**Stellar properties:** mass, radius, effective temperature, metallicity, surface gravity   
**Planet properties:** radius, mass, semi-major axis, orbital eccentricity, equilibrium temperature    
**System parameters:** number of planets, distance, apparent magnitudes (V and K bands)     
**Measurement uncertainties:** upper/lower error bounds on stellar and planetary values    
**Flags and limits:** indicators for radius/mass limits, controversial detections     


## DATA PROCESSING - 
Non-numerical or string features (like pl_name, hostname, disposition) are removed during preprocessing, leaving only numeric data suitable for the neural network.
Non-numeric columns removed: pl_name, hostname, disposition, etc., leaving only numeric features.
NaN values handled: replaced with 0 after standardization.
Standardization: features scaled with StandardScaler to zero mean and unit variance.
Train/test split: stratified to preserve class balance.
Class imbalance addressed: applied class weights during model training instead of undersampling or oversampling.
Final input data: normalized numeric matrix (X_train_normalized, X_test_normalized) and binary labels (y_train, y_test).


## 📦 Setup Instructions
[Playground](https://colab.research.google.com/drive/1KqPKqPoVj_znV-4Hble0yDQ4oLJCee63?usp=sharing)
**Front End UI link**
