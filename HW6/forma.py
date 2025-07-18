import math

MOD = 10**9 + 7


def count_combinations(n, k):
    # Using the formula for combinations: n! / (k! * (n-k)!)
    numerator = math.factorial(n)
    denominator = math.factorial(k) * math.factorial(n-k)
    # Use modular inverse to compute the result modulo MOD
    result = numerator * pow(denominator, MOD-2, MOD) % MOD
    return result


# Example usage:
n = 5
k = 3
num_combinations = count_combinations(n, k)
print(
    f"There are {num_combinations} ways to choose {k} elements from a set of {n} elements.")
