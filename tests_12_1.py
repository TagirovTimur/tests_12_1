import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test = runner.Runner('walk_test')
        for i in range(10):
            test.walk()
        self.assertEqual(test.distance, 50)

    def test_run(self):
        test = runner.Runner('run_test')
        for i in range(10):
            test.run()
        self.assertEqual(test.distance, 100)

    def test_challenge(self):
        test_1 = runner.Runner('walk_test')
        test_2 = runner.Runner('run_test')
        for i in range(10):
            test_1.walk()
            test_2.run()
        self.assertNotEqual(test_1.distance,test_2.distance)

if __name__ == "__main__":
    unittest.main()