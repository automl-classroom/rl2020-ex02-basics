import numpy as np

class MarsRover:
    def __init__(self, transition_probabilities=np.ones((5,2)), rewards=[1, 0, 0, 0, 10], horizon=10):
        self.rewards = rewards
        self.probs = transition_probabilities
        self.c_steps = 0
        self.horizon = horizon

    def reset(self):
        self.c_steps = 0
        self.position = 2
        return self.position

    def step(self, action):
        done = False
        self.c_steps += 1
        follow_action = np.random.choice([0, 1], p=[1-self.probs[self.position][action],self.probs[self.position][action]])
        if not follow_action:
            action = 1 - action

        if action == 0:
            if self.position > 0:
                self.position -= 1
        elif action == 1:
            if self.position < 4:
                self.position += 1
        else:
            print("Not a valid action")
            return
        reward = self.rewards[self.position]
        return self.position, reward, self.c_steps >= self.horizon
