import numpy as np
from env import MarsRover


def update_value_function(v, state, new_state, reward, gamma=0.9):
    done = False
    new_v = np.copy(v)
    new_v[state] = reward + gamma * v[new_state]
    if np.linalg.norm((v - new_v), ord=1) <= 0:
        done = True
    return new_v, done


def update_policy(qs, pi, state, new_state, action, reward, gamma=0.9):
    done = False
    qs[state][action] = reward + gamma * (qs[new_state][0] + qs[new_state][1])
    new_pi = [np.random.choice(np.where(qs[state] == np.array(qs)[state].max())[0]) for state in np.arange(len(qs))]
    if np.linalg.norm((np.array(pi) - np.array(new_pi)), ord=1) <= 0:
        done = True
    return qs, new_pi, done


def run_policy_iteration(transition_probabilities=np.ones((5, 2)), rewards=[1, 0, 0, 0, 10], horizon=10):
    env = MarsRover(transition_probabilities, rewards, horizon)
    qs = np.zeros((5, 2))
    pi = np.random.randint(0, 2, size=5)

    done = False
    state = env.reset()
    i = 0
    while not done:
        i += 1
        print(f"This is step {i}")
        action = pi[state]
        new_state, reward, done = env.step(action)
        qs, pi, converged = update_policy(qs, pi, state, new_state, action, reward)
        if converged:
            break
        state = new_state

    final_reward = evaluate_policy(pi, env)

    print(f"Your policy achieved a final accumulated reward of {final_reward} after {i} update steps.")

    return pi, i, final_reward


def run_value_iteration(transition_probabilities=np.ones((5, 2)) * 0.5, rewards=[1, 0, 0, 0, 10], horizon=10,
                        gamma=0.9):
    v = np.zeros(5)
    env = MarsRover(transition_probabilities, rewards, horizon)
    done = False
    state = env.reset()
    i = 0
    while not done:
        i += 1
        print(f"This is step {i}")
        r1 = (rewards[state - 1] + gamma * v[state - 1])
        r2 = (rewards[state + 1] + gamma * v[state + 1])
        action = np.argmax([r1, r2])
        if r1 == r2:
            action = np.random.randint(2)
        new_state, reward, done = env.step(action)
        v, converged = update_value_function(v, state, new_state, reward)
        if converged:
            break
        state = new_state

    final_reward = evaluate_agent(v, env)

    print(f"Your agent achieved a final accumulated reward of {final_reward} after {i} update steps.")

    return v, i, final_reward


def evaluate_policy(pi, env):
    state = env.reset()
    done = False
    r_acc = 0
    while not done:
        action = pi[state]
        new_state, reward, done = env.step(action)
        r_acc += reward
    return r_acc


def evaluate_agent(v, env):
    state = env.reset()
    done = False
    r_acc = 0
    while not done:
        action = max(v[max(state - 1, 0)], v[min(state + 1, 5)])
        new_state, reward, done = env.step(action)
        r_acc += reward
    return r_acc
