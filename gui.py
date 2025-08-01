import tkinter as tk
from tkinter import ttk, messagebox
import random
import math

class WeatherHandler:
    def get_weather(self, location):
        return {
            "location": location,
            "wind_speed": round(random.uniform(10, 70), 2),
            "visibility": round(random.uniform(1, 10), 2),
            "storm": random.choice([True, False])
        }

class AirTrafficController:
    def __init__(self):
        self.aircrafts = []

    def add_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)

    def detect_conflicts(self):
        conflicts = []
        for i in range(len(self.aircrafts)):
            for j in range(i + 1, len(self.aircrafts)):
                a1, a2 = self.aircrafts[i], self.aircrafts[j]
                dist = math.sqrt((a1['lat'] - a2['lat']) ** 2 + (a1['lon'] - a2['lon']) ** 2)
                alt_diff = abs(a1['altitude'] - a2['altitude'])

                if dist < 1.0 and alt_diff < 1000:
                    conflicts.append((a1, a2))
        return conflicts

    def resolve_conflicts(self, conflicts, weather_handler):
        resolved_routes = []
        for a1, a2 in conflicts:
            weather1 = weather_handler.get_weather((a1['lat'], a1['lon']))
            weather2 = weather_handler.get_weather((a2['lat'], a2['lon']))

            if weather1['storm']:
                a1['altitude'] += 1000
            else:
                a1['heading'] += 5

            if weather2['storm']:
                a2['altitude'] -= 1000
            else:
                a2['heading'] -= 5

            resolved_routes.append((a1.copy(), a2.copy()))
        return resolved_routes

class AirTrafficGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(" Air Traffic AI GUI")
        self.root.geometry("780x600")
        self.controller = AirTrafficController()
        self.weather = WeatherHandler()

        self._setup_widgets()

    def _setup_widgets(self):
        self.frame = ttk.LabelFrame(self.root, text="Aircraft Info")
        self.frame.pack(padx=10, pady=10, fill="x")

        labels = ["ID", "Latitude", "Longitude", "Altitude", "Speed", "Heading"]
        self.entries = {}
        for idx, label in enumerate(labels):
            ttk.Label(self.frame, text=label).grid(row=0, column=idx)
            entry = ttk.Entry(self.frame, width=10)
            entry.grid(row=1, column=idx)
            self.entries[label.lower()] = entry

        ttk.Button(self.frame, text="➕ Add Aircraft", command=self.add_aircraft).grid(row=1, column=6, padx=10)

        self.aircraft_display = tk.Text(self.root, height=8, state='disabled')
        self.aircraft_display.pack(padx=10, pady=5, fill="x")

        self.conflict_btn = ttk.Button(self.root, text="⚠️ Detect Conflicts", command=self.detect_conflicts)
        self.conflict_btn.pack(pady=10)

        self.output_display = tk.Text(self.root, height=20, state='disabled', bg="#f2f2f2")
        self.output_display.pack(padx=10, pady=5, fill="both", expand=True)

    def add_aircraft(self):
        try:
            ac = {
                'id': self.entries['id'].get(),
                'lat': float(self.entries['latitude'].get()),
                'lon': float(self.entries['longitude'].get()),
                'altitude': int(self.entries['altitude'].get()),
                'speed': int(self.entries['speed'].get()),
                'heading': int(self.entries['heading'].get())
            }
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
            return

        self.controller.add_aircraft(ac)
        self._log_aircraft(ac)

    def _log_aircraft(self, ac):
        self.aircraft_display.config(state='normal')
        self.aircraft_display.insert(tk.END, f"Added Aircraft: {ac['id']} at ({ac['lat']}, {ac['lon']}), Alt: {ac['altitude']}, Heading: {ac['heading']}\n")
        self.aircraft_display.config(state='disabled')

    def detect_conflicts(self):
        conflicts = self.controller.detect_conflicts()
        self.output_display.config(state='normal')
        self.output_display.delete("1.0", tk.END)

        if not conflicts:
            self.output_display.insert(tk.END, "No conflicts detected.\n")
        else:
            self.output_display.insert(tk.END, f" Detected {len(conflicts)} conflict(s):\n")
            for a1, a2 in conflicts:
                self.output_display.insert(tk.END, f"  - {a1['id']}  {a2['id']}\n")

            resolved = self.controller.resolve_conflicts(conflicts, self.weather)
            self.output_display.insert(tk.END, "\n Resolved Routes:\n")
            for a1, a2 in resolved:
                self.output_display.insert(tk.END, f"  - {a1['id']} → Alt: {a1['altitude']}, Heading: {a1['heading']}\n")
                self.output_display.insert(tk.END, f"  - {a2['id']} → Alt: {a2['altitude']}, Heading: {a2['heading']}\n")

        self.output_display.config(state='disabled')
