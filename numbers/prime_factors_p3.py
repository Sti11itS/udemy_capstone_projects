"""Returns all Prime Factors (if any) from given number

Takes in non-negative integer 'n' and returns a list of Prime Factors using
Trial Division.

If run directly it interactively asks for inputs. Otherwise the
trial_division(n) function can be imported.
"""

### https://docs.python.org/3/library/typing.html
### https://en.wikipedia.org/wiki/Trial_division


def trial_division(n: int) -> list[int]:
    """Returns list of Prime Factors of given integer 'n'."""
    a = []                  # Prepare an empty list
    while n % 2 == 0:       # While-loop to factor out
        a.append(2)         # all even factors of 'n'
        n //= 2
    f = 3                   # Initiate first odd trial factor (3)
    while f * f <= n:       # While-loop to factor out
        if n % f == 0:      # subsequent prime factors of 'n'
            a.append(f)
            n //= f         # Integer division
        else:
            f += 2          # Add (2) to check next odd factor
    if n != 1:
        a.append(n)

    return a


if __name__ == "__main__":
    # Get non-negative integer 'n' from input
    while True:
        try:
            n = int(input('Enter non-negative integer for Prime ' + \
                          'Factorisation: '))
        except ValueError:
            print('Value needs to be non-negative integer.')
        else:
            if n < 0:
                print('Value needs to be non-negative integer.')
            else:
                break

    # Print result
    print(trial_division(n))
