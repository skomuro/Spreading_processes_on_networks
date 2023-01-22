import numpy as np
import random


def stochastic_one_simulation(gamma, tau):
    states = [[999, 1, 0]]
    ts = [0]
    t_max = 30
    t = 0
    state = states[-1] #Initial states


    while t < t_max:
        state = states[-1]
        t = ts[-1]
        T = state[0] * state[1] * tau + state[1] * gamma
        t_next = random.expovariate(T)
        t = t + t_next
        if random.random() < state[1] * gamma / T:
            new_state = [state[0], state[1] - 1, state[2] + 1]
        else:
            new_state = [state[0] - 1, state[1] + 1, state[2]]
        if new_state[1] == 0:
            break
        ts.append(t)
        states.append(new_state)

    s = [state[0] for state in states]
    i = [state[1] for state in states]
    r = [state[2] for state in states]

    return s, i, r, ts
