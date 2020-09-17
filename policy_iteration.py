from env import MarsRover

#TODO: complete this method
def update_policy():
    return new_pi, converged

#TODO: complete this method
def run_policy_iteration(transition_probabilities=[[0, 1] for _ in range 5], rewards=[1, 0, 0, 0, 10], horizon=10):
    env = MarsRover(transition_probabilities, rewards, horizon)
    done = False
    state = env.reset()
    i = 0
    while not done:
        i += 1
        print(f"This is step {i}")
        new_state, reward, done = env.step(action)

    final_reward = evaluate_policy(pi, env)

    print(f"Your policy achieved a final accumulated reward of {final_reward} after {i} update steps.")

    return pi, i, final_reward

def evaluate_policy(pi, env):
    state = env.reset()
    done = False
    r_acc = 0
    while not done:
        action = pi[state]
        new_state, reward, done = env.step(action)
        r_acc += reward
    return r_acc

if __name__ == '__main__':
    print(run_value_iteration())
