from find_primitive_root_simple import *

find_order_coverage = {
    "a_and_n_are_1": False,
    "gcd_not_1": False,
    "order_found": False
}

euler_totient_coverage = {
    "divisor_found": False,
    "remaining_prime": False
}

find_primitive_root_coverage = {
    "n_is_1": False,
    "coprime_with_n": False,
    "primitive_root_exists": False,
}

def print_coverage(coverage_keys):
    for key, value in coverage_keys.items():
        print(f"The branch {key}: {value}")


def main():
    print("Coverage for the function find_order:")
    find_order(1, 1, find_order_coverage)  # a and n are 1 (a_and_n_are_1)
    print_coverage(find_order_coverage)

    print()

    find_order(2, 4, find_order_coverage)  # gcd not 1 (gcd_not_1)
    print_coverage(find_order_coverage)

    print()

    find_order(3, 7, find_order_coverage)  # order found (order_found)
    print_coverage(find_order_coverage)

    print("\nCoverage for the function euler_totient:")

    euler_totient(9, euler_totient_coverage)  # divisor found (divisor_found)
    print_coverage(euler_totient_coverage)

    print()

    euler_totient(21, euler_totient_coverage)  # remaining prime (remaining_prime) and divisor found (divisor_found)
    print_coverage(euler_totient_coverage)

    print("\nCoverage for the function find_primitive_root:")
    find_primitive_root(1, find_primitive_root_coverage, find_order_coverage, euler_totient_coverage)  # n is 1 (n_is_1)
    print_coverage(find_primitive_root_coverage)

    print()

    find_primitive_root(7, find_primitive_root_coverage, find_order_coverage, euler_totient_coverage)  # coprime with n and coprime_with_n
    print_coverage(find_primitive_root_coverage)


if __name__ == "__main__":
    main()