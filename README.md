# 🌦️ Weather CLI Application

A simple and clean command-line application built in Python that fetches real-time weather data using the Open-Meteo API.

---

## 🚀 Overview

This project demonstrates how to build a modular and maintainable CLI application that:

* Accepts user-provided geographic coordinates
* Fetches real-time weather data from a public API
* Processes and displays key weather information in a clear format

---

## ✨ Features

* Input latitude and longitude via CLI
* Fetch current weather data from Open-Meteo API
* Display:
  * Temperature (°C)
  * Wind Speed (km/h)
  * Weather Condition (human-readable)
* Error handling for invalid inputs and API failures
* Modular code structure (services, utils, CLI)

---

## ⚙️ Installation

### 1. Clone the repository

~~~bash
git clone https://github.com/your-username/weather-cli.git
cd weather-cli
~~~

### 2. Create virtual environment (recommended)

~~~bash
python -m venv venv

# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
~~~

### 3. Install dependencies

~~~bash
pip install -r requirements.txt
~~~

---

## ▶️ Usage

The application can be used in two different modes: **CLI mode** or **Web interface mode**.

### 🖥️ CLI Mode (default)

Run the application:

~~~bash
python main.py
~~~

Then input coordinates when prompted:

~~~
Enter latitude: 41.15
Enter longitude: -8.61
~~~

### 🌐 Web Interface Mode

Run the application in web mode:

~~~bash
python main.py --web
~~~

Then open your browser and access:

~~~
http://127.0.0.1:5000
~~~

Enter the coordinates in the web form to get the weather information.

---

### Example Output (CLI)

~~~
--- Current Weather ---
Temperature: 21.3°C
Wind Speed: 12.5 km/h
Condition: Partly cloudy
~~~

---

## 📦 Requirements

* Python 3.14+
* requests
* flask
