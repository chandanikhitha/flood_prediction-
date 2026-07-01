from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

# ✅ Safe model load
model = None
if os.path.exists("model.pkl"):
    model = pickle.load(open("model.pkl", "rb"))

# ✅ Home page
@app.route("/")
def home():
    return render_template("index.html")

# ✅ Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return "Model not loaded!"

    try:
        rainfall = float(request.form['rainfall'])
        temperature = float(request.form['temperature'])

        prediction = model.predict([[rainfall, temperature]])[0]

        return render_template("index.html", prediction_text=f"Prediction: {prediction}")

    except Exception as e:
        return f"Error: {str(e)}"

# ✅ Run app (local testing)
if __name__ == "__main__":
    app.run(debug=True)
    
