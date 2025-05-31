def prime_check(n,coverage_keys):
    """Return True if n is a prime number
    Else return False.
    """

    if n <= 1:
        coverage_keys["non_positive_or_1"] = True
        return False
    if n == 2 or n == 3:
        coverage_keys["equal_2_or_3"] = True
        return True
    if n % 2 == 0 or n % 3 == 0:
        coverage_keys["even_or_divisible_by_3"] = True
        return False
    j = 5
    while j * j <= n:
        if n % j == 0 or n % (j + 2) == 0:
            coverage_keys["6k±1_form"] = True
            return False
        j += 6

    coverage_keys["prime"] = True  
    return True
