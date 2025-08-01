class AIEngine:
    def resolve_conflicts(self, conflicts, weather):
        resolved = []
        for ac1, ac2 in conflicts:
            # Simplified AI decision: change altitude or heading
            if weather["storm"]:
                ac1['heading'] += 10
                ac2['heading'] -= 10
            else:
                ac1['alt'] += 500
                ac2['alt'] -= 500
            resolved.append((ac1, ac2))
        return resolved
