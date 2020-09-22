import unittest
import numpy as np
#from value_iteration import run_value_iteration, update_value_function
from solutions import run_value_iteration, update_value_function

class TestValueIteration(unittest.TestCase):

    def test_value_quality(self):
        r = []
        steps = []
        for _ in range(10):
            v, i, final_reward = run_value_iteration()
            r.append(final_reward)
            steps.append(i)
        self.assertTrue(np.mean(steps) == 1)
        self.assertTrue(sum(r) > 0)

    def test_single_update(self):
        new_v, converged = update_value_function([0, 0], 0, 1, 1, 10)
        self.assertTrue(new_v[0] > 0)
        self.assertFalse(converged)

    def test_convergence(self):
        _, converged = update_value_function([0, 0], 0, 1, 1, 10)
        self.assertTrue(converged)
        _, converged = update_value_function([0, 0], 0, 1, 1, 10)
        self.assertTrue(converged)
        _, converged = update_value_function([0, 0], 0, 1, 1, 10)
        self.assertTrue(converged)

if __name__ == '__main__':
    unittest.main()
