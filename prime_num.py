def is_prime(number):
    """Returns True if the number is prime, False otherwise."""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def get_primes(n):
    """Returns a list of all prime numbers up to n (inclusive)."""
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage:
n = int(input("Enter a number: "))
prime_numbers = get_primes(n)
print(f"Prime numbers up to {n}: {prime_numbers}")
