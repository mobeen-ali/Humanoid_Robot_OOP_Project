import random

class Environment:
    def detect_obstacle(self):
        """Simulates obstacle detection (50% chance)."""
        return random.choice([True, False])
