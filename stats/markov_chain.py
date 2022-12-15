import matplotlib.pyplot as plt
import numpy as np
import random



class MarkovChain:
    def __init__(self, mat, dist, state=None):
        self.mat = np.array(mat)
        self.dist = np.array(dist)
        self.sz = len(mat)
        if state is None:
            self.collapse()
        else:
            self.state = state
    
    def step(self):
        self.dist @= self.mat
        # no longer certain what the state is
        self.state = None
    
    def collapse(self):
        x = np.random.random()
        for i, prob in enumerate(self.dist):
            if x < prob:
                self.state = i
                self.dist = [0.0] * self.sz
                self.dist[i] = 1.0
                return i
            x -= prob
    
    def simulate(self, trials):
        states = [0.0] * trials
        states[0] = self.collapse()

        for i in range(1, trials):
            self.step()
            states[i] = self.collapse()
        
        return states
    
    def plot_sim(self, states):
        plt.plot(states)
        plt.show()

    # state should not be None
    # steps and collapses
    def step_collapse(self):
        x = np.random.random()
        self.dist @= self.mat
        for i, prob in enumerate(self.dist):
            if x < prob:
                self.state = i
                self.dist = [0.0] * self.sz
                self.dist[i] = 1.0
                break
            x -= prob  

a = np.array([[0.3, 0.7],
              [0.7, 0.3]])


m = MarkovChain(a, [0.5, 0.5])
m.plot_sim(m.simulate(100))