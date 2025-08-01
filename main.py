from traffic_manager import TrafficManager
from weather_handler import WeatherHandler
from ai_engine import AIEngine

# Initialize modules
traffic = TrafficManager()
weather = WeatherHandler()
ai = AIEngine()

# Sample aircraft data (ID, Lat, Lon, Altitude, Speed, Heading)
aircrafts = [
    {"id": "A1", "lat": 23.81, "lon": 90.41, "alt": 30000, "speed": 480, "heading": 90},
    {"id": "A2", "lat": 23.80, "lon": 90.42, "alt": 30500, "speed": 460, "heading": 91},
]

# Simulate weather
weather_data = weather.get_weather("Dhaka")

# Conflict Detection and Rerouting
for aircraft in aircrafts:
    traffic.add_aircraft(aircraft)

conflicts = traffic.detect_conflicts()
rerouted = ai.resolve_conflicts(conflicts, weather_data)

print("\nResolved Routes:")
for route in rerouted:
    print(route)
