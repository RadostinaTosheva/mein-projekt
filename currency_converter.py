import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Funktion zum Abrufen des Wechselkurses
def get_exchange_rate(base_currency, target_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()
        return data["rates"].get(target_currency, None)
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Abrufen der Wechselkurse: {e}")
        return None

# Funktion zur Umrechnung der Währung
def convert_currency():
    base_currency = from_currency.get()
    target_currency = to_currency.get()
    
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Fehler", "Bitte eine gültige Zahl eingeben!")
        return

    rate = get_exchange_rate(base_currency, target_currency)
    
    if rate:
        converted_amount = amount * rate
        result_label.config(text=f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    else:
        messagebox.showerror("Fehler", "Ungültige Währung oder kein Wechselkurs gefunden.")

# GUI erstellen
root = tk.Tk()
root.title("Währungsumrechner")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Stil für das Dropdown-Menü
style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox", fieldbackground="#ffffff", background="#d1d1d1")

# Währungen
currencies = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "BGN"] 

# Titel
title_label = tk.Label(root, text="💰 Währungsumrechner", font=("Arial", 16, "bold"), fg="#333", bg="#f0f0f0")
title_label.pack(pady=10)

# Betrag eingeben
tk.Label(root, text="Betrag:", font=("Arial", 12), bg="#f0f0f0").pack()
amount_entry = tk.Entry(root, font=("Arial", 12), bg="white", justify="center")
amount_entry.pack(pady=5)

# Ausgangswährung wählen
tk.Label(root, text="Von Währung:", font=("Arial", 12), bg="#f0f0f0").pack()
from_currency = ttk.Combobox(root, values=currencies, state="readonly", font=("Arial", 12))
from_currency.pack(pady=5)
from_currency.current(0)

# Zielwährung wählen
tk.Label(root, text="In Währung:", font=("Arial", 12), bg="#f0f0f0").pack()
to_currency = ttk.Combobox(root, values=currencies, state="readonly", font=("Arial", 12))
to_currency.pack(pady=5)
to_currency.current(1)

# Button für die Umrechnung
convert_button = tk.Button(root, text="💱 Umrechnen", font=("Arial", 12, "bold"), bg="#007BFF", fg="white", relief="flat", command=convert_currency)
convert_button.pack(pady=10)

# Ergebnis-Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="green", bg="#f0f0f0")
result_label.pack(pady=10)

# Start der GUI
root.mainloop()