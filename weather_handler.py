import random

class WeatherHandler:
    def get_weather(self, location):
        # Mock weather condition
        weather = {
            "location": location,
            "wind_speed": random.uniform(0, 100),
            "visibility": random.uniform(1, 10),
            "storm": random.choice([True, False])
        }
        return weather
