from flask import Flask, request, render_template_string
from services.weather_service import fetch_weather, process_weather

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Weather App</title>
    <style>
        body {
            margin: 0;
            background: linear-gradient(135deg, #74ebd5, #acb6e5);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background: white;
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            width: 350px;
            text-align: center;
        }

        h1 {
            margin-bottom: 20px;
            font-size: 24px;
        }

        input {
            width: 90%;
            padding: 10px;
            margin: 8px 0;
            border: 1px solid #ddd;
            border-radius: 8px;
            outline: none;
        }

        button {
            width: 100%;
            padding: 10px;
            background: #4a90e2;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 10px;
            font-weight: bold;
        }

        button:hover {
            background: #357ABD;
        }

        .card {
            margin-top: 20px;
            padding: 15px;
            border-radius: 12px;
            background: #f7f7f7;
            text-align: left;
        }

        .label {
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Weather App</h1>

    <form method="POST">
        <input name="lat" placeholder="Latitude" required>
        <input name="lon" placeholder="Longitude" required>
        <button type="submit">Get Weather</button>
    </form>

    {% if result %}
    <div class="card">
        <p><span class="label">Temperature:</span> {{ result.temp }}°C</p>
        <p><span class="label">Wind:</span> {{ result.wind }} km/h</p>
        <p><span class="label">Condition:</span> {{ result.condition }}</p>
    </div>
    {% endif %}
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        lat = float(request.form["lat"])
        lon = float(request.form["lon"])

        data = fetch_weather(lat, lon)
        temp, wind, condition = process_weather(data)

        result = type("obj", (), {
            "temp": temp,
            "wind": wind,
            "condition": condition
        })

    return render_template_string(HTML, result=result)

def run_web_app():
    app.run(debug=True)