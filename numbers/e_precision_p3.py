"""Returns Euler's Number e to the n'th digit

Takes in an integer between 0 to 15 to round math.e to
the specified precision.
"""

from math import e


def e_precision():
    """Returns math.e to a specified precision"""
    while True:
        try:
            dec_num = int(input('Enter decimal place for e: '))
        except ValueError:
            print('Value needs to be an integer.')
        else:
            if dec_num < 0 or dec_num > 15:
                print('Value needs to be between 0 (zero) and 15')
            else:
                print(f'Rounding math.e to {dec_num} places.')
                break

    return round(e, dec_num)


if __name__ == "__main__":
    print(e_precision())
