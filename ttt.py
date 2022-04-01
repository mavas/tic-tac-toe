"""
tic-tac-toe

An on-the-fly coding interview problem I did (I had no idea I was going to be
given this, and I did it like this).
"""


import numpy as np


def can_continue(a):
    """Determines if someone wins, or we can continue."""

    # wins..
    for i in (1, 2):
        if a[0][0] == a[0][1] == a[0][2] == i:  # rows
            return False
        if a[1][0] == a[1][1] == a[1][2] == i:
            return False
        if a[2][0] == a[2][1] == a[2][2] == i:
            return False

        if a[0][0] == a[1][0] == a[2][0] == i:  # cols
            return False
        if a[0][1] == a[1][1] == a[2][1] == i:
            return False
        if a[0][2] == a[1][2] == a[2][2] == i:
            return False

        if a[0][0] == a[1][1] == a[2][2] == i:  # diags
            return False
        if a[0][2] == a[1][1] == a[2][0] == i:
            return False

    # valid board..
    for i in range(3):
        if a[0][i] == 0 or a[1][i] == 0 or a[2][i] == 0:
            return True
    for i in range(3):
        if a[1][0] == 0 or a[i][1] == 0 or a[i][2] == 0:
            return True

    # ..
    return False


def tic_tac_toe_game():
    """Plays a tic-tac-toe game between 2 players."""
    a = np.zeros((3, 3), dtype=np.int32)

    t = True
    while can_continue(a):
        print a
        if t: print("Player 1 turn")
        else: print("Player 2 turn")
        valid_choice = False
        while not valid_choice:
            xp = int(input("X: "))
            yp = int(input("Y: "))
            if a[xp][yp] == 0:
                valid_choice = True
            else:
                print("Illegal position: position already has a '{}' in it.".format(a[xp][yp]))
                print('Try again..')
        if t:
            a[xp][yp] = 1
        else:
            a[xp][yp] = 2
        t = not t

    # determine winner..
    for i in (1, 2):
        if a[0][0] == a[0][1] == a[0][2] == i:  # rows
            return i
        if a[1][0] == a[1][1] == a[1][2] == i:
            return i
        if a[2][0] == a[2][1] == a[2][2] == i:
            return i

        if a[0][0] == a[1][0] == a[2][0] == i:  # cols
            return i
        if a[0][1] == a[1][1] == a[2][1] == i:
            return i
        if a[0][2] == a[1][2] == a[2][2] == i:
            return i

        if a[0][0] == a[1][1] == a[2][2] == i:  # diags
            return i
        if a[0][2] == a[1][1] == a[2][0] == i:
            return i


if __name__ == '__main__':
    w = tic_tac_toe_game()
    if w == 1: print("player 1 wins!")
    elif w == 2: print("player 2 wins!")
    else: print("Something went wrong.")
