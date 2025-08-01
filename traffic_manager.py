import math

class TrafficManager:
    def __init__(self):
        self.aircrafts = []

    def add_aircraft(self, aircraft):
        self.aircrafts.append(aircraft)

    def detect_conflicts(self):
        conflicts = []
        for i in range(len(self.aircrafts)):
            for j in range(i+1, len(self.aircrafts)):
                ac1 = self.aircrafts[i]
                ac2 = self.aircrafts[j]
                if self._is_conflict(ac1, ac2):
                    conflicts.append((ac1, ac2))
        return conflicts

    def _is_conflict(self, ac1, ac2):
        dist = math.sqrt((ac1['lat'] - ac2['lat'])**2 + (ac1['lon'] - ac2['lon'])**2)
        alt_diff = abs(ac1['alt'] - ac2['alt'])
        return dist < 0.01 and alt_diff < 1000
