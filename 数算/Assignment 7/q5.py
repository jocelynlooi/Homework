import sys


def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime


def find_primes_with_last_digit_one(is_prime, n):
    primes_with_one = []
    for num in range(2, n):
        if is_prime[num] and num % 10 == 1:
            primes_with_one.append(num)
    return primes_with_one


def main():
    input_data = sys.stdin.read().strip().split('\n')
    T = int(input_data[0])
    test_cases = list(map(int, input_data[1:]))

    max_n = max(test_cases)

    is_prime = sieve_of_eratosthenes(max_n)

    for idx, n in enumerate(test_cases, start=1):
        primes = find_primes_with_last_digit_one(is_prime, n)
        print(f"Case{idx}:")
        if primes:
            print(" ".join(map(str, primes)))
        else:
            print("NULL")


if __name__ == "__main__":
    main()
