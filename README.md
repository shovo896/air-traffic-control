AI-Powered Air Traffic Control & Weather Navigator (Tkinter GUI)

This Python project simulates an AI-assisted Air Traffic Control System with weather-based navigation decisions. It uses a simple graphical interface built with   Tkinter that allows users to:
- Input multiple aircraft data
- Detect conflicts
- Simulate weather conditions
- Automatically resolve issues using basic AI rules

1️. Key Features

1. Add aircraft with position (latitude & longitude), altitude, speed, and heading.
2. Detect conflicts when aircraft are close in space or altitude.
3. Simulate weather factors like wind, visibility, and storms.
4. Use AI rules to resolve traffic conflicts by adjusting heading or altitude.
5. Display results in a user-friendly read-only log section.



 2️.GUI Layout Breakdown

1. Aircraft Info Input Section  
   - Enter aircraft ID, position, speed, heading, etc.
2. Aircraft List Log  
   - Shows all the aircraft added to the system.
3. Conflict Detection Button 
   - Starts conflict detection and resolution.
4. Resolved Routes / Output Display 
   - Shows conflict results and decisions made by the AI.



 3️. Why Output is Read-Only?

The output log is made read-only intentionally using the following line in Tkinter:

python
self.output_display.config(state='disabled')


This is done for three reasons:

1. To preserve log integrit — system-generated logs should not be altered.
2. To maintain professional UI design — read-only logs mimic real air traffic systems.
3. To avoid user errors — editable outputs could lead to confusion or mistakes.

If needed, you can make it editable by changing:

python
self.output_display.config(state='normal')




4️. How to Run the Project

1. Clone the repository:

   bash
   git clone https://github.com/your-username/air-traffic-ai.git
   cd air-traffic-ai
   

2. Make sure Python 3.7+ is installed on your system.

3. Run the application:

   bash
   python main.py
   



 5️. Sample Inputs to Try

Use the following aircraft data to simulate a scenario:

* Aircraft 1:

  * ID: `A101`
  * Latitude: `23.45`
  * Longitude: `90.31`\
  *  Altitude: 30000
  * Speed: `500`
  * Heading: 90
  *
  *

  Aircraft 2:

  * ID: B202
  * Latitude: 23.46
  * Longitude: 90.32
  * Altitude: 30500
  * Speed: 480
  * Heading: 88




 6️.Project Files

1. main.py — Entry point of the app
2. gui.py — All GUI code written in Tkinter
3. README.md — This file



 7️. Possible Future Features

1. Integrate live weather APIs (e.g., OpenWeatherMap)
2. Predict flight paths using machine learning
3. Add real radar visuals using Matplotlib or 3D libraries
4. Export logs to .csv or .json



 8️. License

This project is licensed under the MIT License — you can use, modify, and distribute freely with attribution.





