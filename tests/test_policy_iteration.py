import unittest


class TestValueIteration(unittest.TestCase):

    def test_policy_iteration():
        #First, check that env is not changed
        #Get state, done, etc.
        #Execute pi. At each step check that:
        #It aborts if pi_i == pi_i+1
        #pi matches the value function
        #The values for 1-3 are at most 0
        #The values for 4 0 or positive and 1 should be greater than -2

        #Get an infinite run setup and confirm it runs forever?

        #Get a single iteration setup at check it's a single iteration?


if __name__ == '__main__':
    unittest.main()
