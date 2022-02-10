"""Returns pi to the n'th digit

Takes in an integer between 0 to 15 to round math.pi to the specified
precision.

If run directly it interactively asks for inputs. Otherwise the pi_precision(n)
function can be imported.
"""

from math import pi


def pi_precision(n: int) -> float:
    """Returns math.pi to specified precision 'n'"""
    return round(pi, n)


if __name__ == "__main__":
    # Get integer between 0 to 15
    while True:
        try:
            dec_pl = int(input('Enter decimal place for pi: '))
        except ValueError:
            print('Value needs to be an integer.')
        else:
            if dec_pl < 0 or dec_pl > 15:
                print('Value needs to be between 0 (zero) and 15')
            else:
                print(f'Rounding math.pi to {dec_pl} places.')
                break

    # Print result
    print(pi_precision(dec_pl))
