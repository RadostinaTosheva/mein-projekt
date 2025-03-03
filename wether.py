import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    api_key = "b62eaccfd1a09cf1d04b00bd2ec689e7" # Ersetze mit deinem API-Schlüssel
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=de"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] != 200:
            messagebox.showerror("Fehler", f"Stadt nicht gefunden: {city}")
            return
        
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        weather_label.config(text=f"Temperatur: {temp}°C\n{weather_desc}\nLuftfeuchtigkeit: {humidity}%\nWind: {wind_speed} m/s")
    except Exception as e:
        messagebox.showerror("Fehler", "Fehler beim Abrufen der Wetterdaten")

# GUI erstellen
root = tk.Tk()
root.title("Wetter App")
root.geometry("300x300")

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Wetter abrufen", command=get_weather)
search_button.pack()

weather_label = tk.Label(root, font=("Arial", 12))
weather_label.pack(pady=20)

root.mainloop()