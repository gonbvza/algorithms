import unittest
from algorithms.maths.find_primitive_root_simple import find_order, euler_totient, find_primitive_root

class TestFindPrimitiveRootSimple(unittest.TestCase):
    def test_find_order(self):
        # Test when a and n are 1
        find_order_coverage = {}
        self.assertEqual(find_order(1, 1, find_order_coverage), 1)
        self.assertTrue(find_order_coverage.get("a_and_n_are_1", False))
        
        # Test when gcd(a, n) != 1
        find_order_coverage = {}
        self.assertEqual(find_order(2, 4, find_order_coverage), -1)
        self.assertTrue(find_order_coverage.get("gcd_not_1", False))
        
        # Test when order is found
        find_order_coverage = {}
        self.assertEqual(find_order(3, 7, find_order_coverage), 6)
        self.assertTrue(find_order_coverage.get("order_found", False))
        
        # Additional test cases
        find_order_coverage = {}
        self.assertEqual(find_order(2, 7, find_order_coverage), 3)
        self.assertTrue(find_order_coverage.get("order_found", False))

        # Test when order is not found
        find_order_coverage = {}
        self.assertEqual(find_order(2, 1, find_order_coverage), -1)
        self.assertTrue(find_order_coverage.get("order_not_found", False))

        
    def test_euler_totient(self):
        # Test when divisor is found
        euler_totient_coverage = {}
        self.assertEqual(euler_totient(9, euler_totient_coverage), 6)
        self.assertTrue(euler_totient_coverage.get("divisor_found", False))
        
        # Test when remaining prime exists
        euler_totient_coverage = {}
        self.assertEqual(euler_totient(21, euler_totient_coverage), 12)
        self.assertTrue(euler_totient_coverage.get("divisor_found", False))
        self.assertTrue(euler_totient_coverage.get("remaining_prime", False))
        
        # Additional test cases
        euler_totient_coverage = {}
        self.assertEqual(euler_totient(7, euler_totient_coverage), 6)
        self.assertTrue(euler_totient_coverage.get("remaining_prime", False))
        
    def test_find_primitive_root(self):
        # Test when n is 1
        find_primitive_root_coverage = {}
        find_order_coverage = {}
        euler_totient_coverage = {}
        self.assertEqual(find_primitive_root(1, find_primitive_root_coverage, find_order_coverage, euler_totient_coverage), [0])
        self.assertTrue(find_primitive_root_coverage.get("n_is_1", False))
        
        # Test when coprime with n exists and primitive root exists
        find_primitive_root_coverage = {}
        find_order_coverage = {}
        euler_totient_coverage = {}
        self.assertEqual(find_primitive_root(7, find_primitive_root_coverage, find_order_coverage, euler_totient_coverage), [3, 5])
        self.assertTrue(find_primitive_root_coverage.get("coprime_with_n", False))
        self.assertTrue(find_primitive_root_coverage.get("primitive_root_exists", False))
        
        # Additional test cases
        find_primitive_root_coverage = {}
        find_order_coverage = {}
        euler_totient_coverage = {}
        result = find_primitive_root(11, find_primitive_root_coverage, find_order_coverage, euler_totient_coverage)
        self.assertEqual(set(result), {2, 6, 7, 8})
        self.assertTrue(find_primitive_root_coverage.get("coprime_with_n", False))
        self.assertTrue(find_primitive_root_coverage.get("primitive_root_exists", False))

if __name__ == '__main__':
    unittest.main()