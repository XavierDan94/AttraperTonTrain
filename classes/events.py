import random


class Events:
    def __init__(self):
        self.incident_occurrence = random.randint(1, 100)
        self.incident = False
        if self.incident_occurrence <= 10:  # Probability of getting an incident
            self.incident = True
