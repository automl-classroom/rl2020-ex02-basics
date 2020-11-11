import unittest

class TestQuestions(unittest.TestCase):

    def test_questions(self):
        with open('observations.txt') as fh:
            lines = fh.readlines()

        self.assertTrue(lines[0].startswith('1') or lines[0].startswith('One') or lines[0].startswith('one'))
        self.assertTrue(lines[1].startswith('reward') or lines[1].startswith('Reward') or lines[1].startswith('R ') or lines[1].startswith('The reward'))
        self.assertTrue(lines[2].startswith('v'))
        self.assertTrue(lines[3].startswith('p'))
        self.assertTrue(lines[4].startswith('Yes') or lines[4].startswith('yes'))


if __name__ == '__main__':
    unittest.main()
