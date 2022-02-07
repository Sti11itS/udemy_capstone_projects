"""Returns pi to the n'th digit

Takes in an integer between 0 to 15 to round math.pi to
the specified precision.
"""

from math import pi

def pi_precision():
    """Returns math.pi to specified precision"""
    while True:
        try:
            dec_num = int(input('Enter decimal place for pi: '))
        except ValueError:
            print('Value needs to be an integer.')
        else:
            if dec_num < 0 or dec_num > 15:
                print('Value needs to be between 0 (zero) and 15')
            else:
                print(f'Rounding math.pi to {dec_num} places.')
                break

    return round(pi, dec_num)

if __name__ == "__main__":
    print(pi_precision())
