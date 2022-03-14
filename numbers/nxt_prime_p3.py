"""Return the next Prime Number until user requests to stop

Yields the next Prime Number starting from 2

If run directly it interactively asks for inputs. Otherwise the genPrime()
generator can be imported.
"""


def is_prime(n: int) -> bool:
    """Checks for Prime"""
    if n > 1:                                     # Check for negatives
        if n == 2:                                # Check for number 2
            return True
        if n % 2 == 0:                            # Check for even
            return False
        for div in range(3, int((n**0.5)+1), 2):  # Check rest, up to sqrt of n
            if n % div == 0:
                return False
        return True
    return False  # Note: 0 and 1 are not Primes


def genPrime() -> int:
    """Generates Prime Numbers until stopped, starts from 2."""
    yield 2
    num = 3
    while True:
        if is_prime(num):
            yield num
        num += 2


if __name__ == "__main__":
    print("Press Enter to generate next Prime Number, 's' to stop.")
    gen = genPrime()

    # Generate Prime Number until stopped using 's'
    while True:
        ans = input()
        if ans == 's':
            break
        print(next(gen), end='')
