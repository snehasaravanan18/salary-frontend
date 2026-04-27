from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

api_url = "https://salary-api-sneha-d4cmdmgrbjd3e4eg.centralus-01.azurewebsites.net/predict"

html = """
<h2>Sneha Saravanan - Salary Predictor</h2>

<form action="/predict" method="POST">

    <label>Education</label>
    <select name="education" required>
        <option value="">Please choose an option</option>
        <option value="0">Bachelors</option>
        <option value="1">Masters</option>
    </select>

    <br><br>

    <label>Experience</label>
    <select name="experience" required>
        <option value="">Please choose an option</option>
        <option value="0">0-2 years</option>
        <option value="1">3+ years</option>
    </select>

    <br><br>

    <button type="submit">Predict</button>
</form>

{% if prediction %}
    <h3>Prediction: {{ prediction }}</h3>
{% endif %}
"""

@app.route("/")
def home():
    return render_template_string(html)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = {
            "education": int(request.form["education"]),
            "experience": int(request.form["experience"])
        }

        response = requests.post(api_url, json=data)
        result = response.json()

        prediction = result.get("prediction", result)

        return render_template_string(html, prediction=prediction)

    except Exception as e:
        return render_template_string(html, prediction=f"Error: {e}")


# 🚨 THIS LINE IS WHAT YOU ARE MISSING
if __name__ == "__main__":
    print("SERVER STARTING...")   # helps you confirm it runs
    app.run(debug=True)
    