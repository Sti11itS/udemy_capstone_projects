"""Returns total cost of W x H floor from given tile price

Simple calculation to return the total cost to tile a rectangular
shaped W x H floor from a given tile cost.

## TODO: Implement different methods of area calculation.
         Example: Calculation by coodinates
"""


def askValue(s: str) -> float:
    """Returns positive float number from input."""
    while True:
        try:
            val = float(input(f'{s}'))
        except ValueError:
            print('Value needs to be a number.')
        else:
            if val < 0:
                print('Value needs to be a positive value.')
            else:
                break

    return val


def totWHCost(W: float, H: float, ppt: float) -> str:
    """Given W, H and ppt, print total cost."""
    return print(f'The total cost of W x H floor is ${W*H*ppt:<.2f}.')


if __name__ == '__main__':
    # Get W, H and perunit input values
    W = askValue('Enter width "W" units of floor plan: ')
    H = askValue('Enter height "H" units of floor plan: ')
    ppt = askValue('Enter cost per unit tile of floor plan: ')

    # Print total cost of rectangular W x H floor
    totWHCost(W, H, ppt)
