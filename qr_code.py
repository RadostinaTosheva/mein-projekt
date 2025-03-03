import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("QR-Code Generator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        # Label für Eingabe
        tk.Label(root, text="Gib den Text oder Link ein:", font=("Arial", 12)).pack(pady=10)

        # Eingabefeld
        self.entry = tk.Entry(root, font=("Arial", 12), width=40)
        self.entry.pack(pady=5)

        # Button zum Generieren des QR-Codes
        tk.Button(root, text="QR-Code generieren", command=self.generate_qr, font=("Arial", 12)).pack(pady=10)

        # Canvas für QR-Code-Anzeige
        self.canvas = tk.Label(root)
        self.canvas.pack(pady=10)

        # Button zum Speichern des QR-Codes
        tk.Button(root, text="QR-Code speichern", command=self.save_qr, font=("Arial", 12)).pack(pady=10)

    def generate_qr(self):
        """Generiert einen QR-Code und zeigt ihn im GUI-Fenster an."""
        data = self.entry.get().strip()
        if not data:
            messagebox.showerror("Fehler", "Bitte gib einen Text oder Link ein!")
            return

        # QR-Code erstellen
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill="black", back_color="white")
        self.qr_img = img  # Speichern für spätere Verwendung

        # Bild für Tkinter anzeigen
        img = img.resize((200, 200))  # Größe anpassen
        self.tk_img = ImageTk.PhotoImage(img)
        self.canvas.config(image=self.tk_img)

    def save_qr(self):
        """Speichert den generierten QR-Code als Bilddatei."""
        if not hasattr(self, "qr_img"):
            messagebox.showerror("Fehler", "Bitte erst einen QR-Code generieren!")
            return

        filepath = filedialog.asksaveasfilename(defaultextension=".png",
                                                filetypes=[("PNG Datei", "*.png"),
                                                           ("JPEG Datei", "*.jpg"),
                                                           ("Alle Dateien", "*.*")])
        if filepath:
            self.qr_img.save(filepath)
            messagebox.showinfo("Erfolg", f"QR-Code gespeichert als {filepath}")

# Starte das Programm
root = tk.Tk()
app = QRCodeGenerator(root)
root.mainloop()