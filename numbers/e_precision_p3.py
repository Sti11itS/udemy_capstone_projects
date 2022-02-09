"""Returns Euler's Number e to the n'th digit

Takes in an integer between 0 to 15 to round math.e to the specified precision.

If run directly it interactively asks for inputs. Otherwise the e_precision(n)
function can be imported.
"""

from math import e


def e_precision(n):
    """Returns math.e to a specified precision 'n'"""
    return round(e, n)


if __name__ == "__main__":
    # Get integer between 0 to 15
    while True:
        try:
            dec_pl = int(input('Enter decimal place for e: '))
        except ValueError:
            print('Value needs to be an integer.')
        else:
            if dec_pl < 0 or dec_pl > 15:
                print('Value needs to be between 0 (zero) and 15')
            else:
                print(f'Rounding math.e to {dec_pl} places.')
                break

    # Print result
    print(e_precision(dec_pl))
