import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# API CONFIGURATION
# -----------------------------
API_KEY = "05de80774ade0c4b69bbd8576ce0de1d"
CITY = "Chennai"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# -----------------------------
# FETCH DATA FROM API
# -----------------------------
response = requests.get(URL)
data = response.json()

print(data)

# -----------------------------
# DATA PROCESSING
# -----------------------------
dates = []
temperatures = []
humidity = []

for entry in data["list"]:
    dates.append(entry["dt_txt"])
    temperatures.append(entry["main"]["temp"])
    humidity.append(entry["main"]["humidity"])

df = pd.DataFrame({
    "Date": dates,
    "Temperature (°C)": temperatures,
    "Humidity (%)": humidity
})

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# DATA VISUALIZATION
# -----------------------------
sns.set(style="whitegrid")

plt.figure(figsize=(12, 6))
sns.lineplot(x="Date", y="Temperature (°C)", data=df, label="Temperature")
sns.lineplot(x="Date", y="Humidity (%)", data=df, label="Humidity")

plt.title(f"5-Day Weather Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Values")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("weather_dashboard.png")
plt.show()
