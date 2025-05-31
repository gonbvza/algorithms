from prime_check import *

prime_check_coverage = {
    "non_positive_or_1": False,
    "equal_2_or_3": False,
    "even_or_divisible_by_3": False,
    "6k±1_form": False,
    "prime": False
}

def print_coverage(coverage_keys):
    for key, value in coverage_keys.items():
        print(f"The branch {key}: {value}")

def main():

    print("Coverage for the function prime_check:")


    prime_check(-1, prime_check_coverage)  # Non-positive number (non_positive_or_1)
    print_coverage(prime_check_coverage)

    prime_check(2, prime_check_coverage)   # 2 is prime (equal_2_or_3)
    print_coverage(prime_check_coverage)

    prime_check(4, prime_check_coverage)   # 4 is not prime (even or divisible by 3)
    print_coverage(prime_check_coverage)

    prime_check(5, prime_check_coverage)   # 5 is prime (6k±1_form)
    print_coverage(prime_check_coverage)

    prime_check(29, prime_check_coverage)  # 29 is prime (prime exiting loop)
    print_coverage(prime_check_coverage)


if __name__ == "__main__":
    main()