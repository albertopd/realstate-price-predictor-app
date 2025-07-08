# 🏠 Real Estate Price Predictor App

This is a **Streamlit** web application that predicts real estate property prices based on user inputs. It leverages a **FastAPI** machine learning model hosted at:

[https://challenge-api-deployment-13tu.onrender.com](https://challenge-api-deployment-13tu.onrender.com)

---

## 🚀 Features

- Input property details such as type, subtype, location, surface areas, room counts, and amenities.
- Dropdowns and sliders for easy selection.
- Dynamic subtype options based on property type.
- Validations and optional fields.
- Instant price prediction by sending data to the deployed ML API.
- Clear display of prediction or error messages.

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/albertopd/realstate-price-predictor-app.git
cd realstate-price-predictor-app
```

2. Create and activate a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the App

```bash
streamlit run app.py
```

---

## 🧾 Requirements

- python 3.10+
- requests 2.32.4
- streamlit 1.46.1

All required packages are listed in [`requirements.txt`](requirements.txt).

---

## 👥 Contributors

- [Alberto](https://github.com/albertopd)

---
