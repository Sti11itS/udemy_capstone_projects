"""Returns Fibonacci Number F(n) from given n'th number

Takes in non-negative integer 'n' starting from 0 (zero) and returns either the
Fibonacci Numbers up to sequence 'n' or the n'th number.

If run directly it interactively asks for inputs. Otherwise the genfib(n)
generator can be imported.
"""

import itertools


def genfib(n):
    """Generates the Fibonacci Sequence to position 'n' or index 'n+1'"""
    a = 0
    b = 1
    for i in range(n+1):
        yield a
        a, b = b, a+b


if __name__ == "__main__":
    # Get non-negative integer for seq
    while True:
        try:
            seq = int(input('Enter non-negative integer for n\'th number: '))
        except ValueError:
            print('Value needs to be non-negative integer.')
        else:
            if seq < 0:
                print('Value needs to be non-negative integer.')
            else:
                break

    # Get output format: [1] for 1ist or [2] for last element
    while True:
        state = input('Generate the sequence [1] \n' + \
                      'or return n\'th number? [2]: ')
        if state in ['1','2']:
            break

    # Print result
    if state == '1':
        print(f'Printing Fibonacci Sequence up to F({seq}):')
        print(list(genfib(seq)))
    elif state == '2':
        print(f'Printing Fibonacci Number at F({seq}):')
        print(list(itertools.islice(genfib(seq), seq, seq+1))[0])

    ### For Python 3.10 ###
    # match state:
    #     case '1':
    #         print(list(genfib(n)))
    #     case '2':
    #         print(list(itertools.islice(genfib(n), n, n+1))[0])
    #######################
