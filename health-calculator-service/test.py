import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):

    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
    
    def test_calculate_bmr_male(self):
        self.assertAlmostEqual(calculate_bmr(175, 70, 25, 'male'), 2626.84, places=2)
    
    def test_calculate_bmr_female(self):
        self.assertAlmostEqual(calculate_bmr(160, 60, 30, 'female'), 1983.09, places=2)


if __name__ == '__main__':
    unittest.main()