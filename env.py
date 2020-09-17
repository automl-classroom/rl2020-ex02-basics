import numpy as np

class MarsRover:
    def __init__(self, transition_probabilities=[[0, 1] for _ in range 5], rewards=[1, 0, 0, 0, 10], horizon=10):
        self.position = starting_position
        self.rewards = rewards
        self.probs = transition_probabilities
        self.c_steps = 0
        self.horizon = horizon

    def reset(self):
        self.c_steps = 0
        self.position = self.starting_position
        return self.position

    def step(self, action):
        done = False
        self.c_steps += 1
        follow_action = np.random.choice([0, 1], p=self.probs[self.position])
        if not follow_action:
            action = 1 - action

        if action == 0:
            if self.position > 0:
                self.position -= 1
        elif action == 1:
            if self.position < 5:
                self.position += 1
        else:
            print("Not a valid action")
            return
        reward = self.rewards[self.position]
        return self.position, reward, self.c_steps >= self.horizon
