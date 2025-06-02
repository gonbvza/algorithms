import unittest
from algorithms.maths.prime_check import prime_check

class TestPrimeCheck(unittest.TestCase):
    def test_non_positive_or_1(self):
        coverage_keys = {}
        self.assertFalse(prime_check(-5, coverage_keys))
        self.assertTrue(coverage_keys.get("non_positive_or_1", False))
        
        coverage_keys = {}
        self.assertFalse(prime_check(0, coverage_keys))
        self.assertTrue(coverage_keys.get("non_positive_or_1", False))
        
        coverage_keys = {}
        self.assertFalse(prime_check(1, coverage_keys))
        self.assertTrue(coverage_keys.get("non_positive_or_1", False))
       
        
    def test_equal_2_or_3(self):
        coverage_keys = {}
        self.assertTrue(prime_check(2, coverage_keys))
        self.assertTrue(coverage_keys.get("equal_2_or_3", False))
        
        coverage_keys = {}
        self.assertTrue(prime_check(3, coverage_keys))
        self.assertTrue(coverage_keys.get("equal_2_or_3", False))
       
        
    def test_even_or_divisible_by_3(self):
        coverage_keys = {}
        self.assertFalse(prime_check(4, coverage_keys))
        self.assertTrue(coverage_keys.get("even_or_divisible_by_3", False))
        
        coverage_keys = {}
        self.assertFalse(prime_check(9, coverage_keys))
        self.assertTrue(coverage_keys.get("even_or_divisible_by_3", False))
        
    def test_six_k_plus_minus_one_form(self):
        coverage_keys = {}
        self.assertFalse(prime_check(25, coverage_keys))
        self.assertTrue(coverage_keys.get("6k±1_form", False))
        
        coverage_keys = {}
        self.assertFalse(prime_check(35, coverage_keys))
        self.assertTrue(coverage_keys.get("6k±1_form", False))
        
    def test_prime(self):
        coverage_keys = {}
        self.assertTrue(prime_check(5, coverage_keys))
        self.assertTrue(coverage_keys.get("prime", False))
        
        coverage_keys = {}
        self.assertTrue(prime_check(17, coverage_keys))
        self.assertTrue(coverage_keys.get("prime", False))
        
        coverage_keys = {}
        self.assertTrue(prime_check(29, coverage_keys))
        self.assertTrue(coverage_keys.get("prime", False))

if __name__ == '__main__':
    unittest.main()