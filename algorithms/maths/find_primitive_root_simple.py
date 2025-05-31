"""
Function to find the primitive root of a number.
"""
import math

"""
For positive integer n and given integer a that satisfies gcd(a, n) = 1,
the order of a modulo n is the smallest positive integer k that satisfies
pow (a, k) % n = 1. In other words, (a^k) ≡ 1 (mod n).
Order of certain number may or may not be exist. If so, return -1.
"""
def find_order(a, n, find_order_coverage):
    """
    Find order for positive integer n and given integer a that satisfies gcd(a, n) = 1.
    Time complexity O(nlog(n))
    """
    if (a == 1) & (n == 1):
        find_order_coverage["a_and_n_are_1"] = True
        # Exception Handeling : 1 is the order of of 1
        return 1
    if math.gcd(a, n) != 1:
        find_order_coverage["gcd_not_1"] = True
        print ("a and n should be relative prime!")
        return -1
    for i in range(1, n):
        if pow(a, i) % n == 1:
            find_order_coverage["order_found"] = True
            return i
    return -1

"""
Euler's totient function, also known as phi-function ϕ(n),
counts the number of integers between 1 and n inclusive,
which are coprime to n.
(Two numbers are coprime if their greatest common divisor (GCD) equals 1).
Code from /algorithms/maths/euler_totient.py, written by 'goswami-rahul'
"""
def euler_totient(n, euler_totient_coverage):
    """Euler's totient function or Phi function.
    Time Complexity: O(sqrt(n))."""
    result = n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            euler_totient_coverage["divisor_found"] = True
            while n % i == 0:
                n //= i
            result -= result // i
    if n > 1:
        euler_totient_coverage["remaining_prime"] = True   
        result -= result // n
    return result

"""
For positive integer n and given integer a that satisfies gcd(a, n) = 1,
a is the primitive root of n, if a's order k for n satisfies k = ϕ(n).
Primitive roots of certain number may or may not exist.
If so, return empty list.
"""
def find_primitive_root(n, find_primitive_root_coverage, find_order_coverage, euler_totient_coverage):
    if n == 1:
        find_primitive_root_coverage["n_is_1"] = True
        # Exception Handeling : 0 is the only primitive root of 1
        return [0]
    phi = euler_totient(n, euler_totient_coverage)
    p_root_list = []
    """ It will return every primitive roots of n. """
    for i in range (1, n):
        #To have order, a and n must be relative prime with each other.
        if math.gcd(i, n) == 1:
            find_primitive_root_coverage["coprime_with_n"] = True
            order = find_order(i, n, find_order_coverage)
            if order == phi:
                find_primitive_root_coverage["primitive_root_exists"] = True
                p_root_list.append(i)
    return p_root_list
