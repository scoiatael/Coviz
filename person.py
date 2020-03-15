import numpy as np


class Person(object):
    def __init__(self, state, sociability, infection_time):
        self.state = state
        self.sociability = sociability
        self.infection_time = infection_time

    def infect(self):
        if self.state == "healthy":
            self.state = "infected"

    def tick(self, recovery_chance):
        if self.state == "infected":
            self.infection_time -= 1
            if self.infection_time == 0:
                if np.random.uniform(0.0, 1.0) <= recovery_chance:
                    self.state = "cured"
                else:
                    self.state = "dead"

    def get_state_letter(self):
        return self.state[0]
