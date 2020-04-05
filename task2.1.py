# task2.1.py implements a hill climbing algorithm to find a solution for the n-queens problem from a random given pos


import random
import sys


def main():
    # input
    n = int(sys.argv[1])  # board dimension given by user
    queens = []

    # 100 iterations each time
    itr = 0
    while itr < 100:
        itr += 1

        # generate random position for all queens
        for i in range(n):
            queens.append(random.randrange(0, n))

        # initial display: iterations, queen board, and num initial attacks
        print("-----Iteration", itr, "-----")
        print('Initial State')
        printQueens(queens, n)
        print("Initial Attacks:", numAttacks(queens, n))

        # hill climb with given queen positions
        hillClimbing(queens, n)
        queens.clear()


# number of attacks per board (counts one attack per pair)
    # q = list of queen positions, n = board dimension (nxn)
def numAttacks(q, n):
    attacks = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if q[i] == q[j]: # checks across
                attacks += 1
            elif q[i] - i == q[j] - j or q[i] + i == q[j] + j: # checks diagonals
                attacks += 1
    return attacks


# show the board of queens
    # q = list of queen positions, n = dimension of board (nxn)
def printQueens(q, n):
    board = [['-' for i in range(n)] for i in range(n)]

    for j in range(n):
        board[q[j]][j] = 'Q'

    print('\n'.join([''.join(['{:2}'.format(item) for item in row])
                     for row in board]))


def hillClimbing(q, n):
    # declare variables
    qBest = q[:]
    qTemp = q[:]
    steps = 0
    initial = numAttacks(q, n)
    best = initial
    attacks = []

    # while still finding a lower value within the last 100 consecutive steps
    while steps < 100:
        for i in range(0, n):
            for j in range(0, n):
                qTemp[j] = i
                temp = numAttacks(qTemp, n) # determine number of attacks in each position
                attacks.append(numAttacks(qTemp, n))

                # find the best (lowest) value
                if temp < best:
                    qBest = qTemp[:]
                    best = temp
                    steps = 0

                else:
                    steps += 1
                    qTemp = qBest[:]


    print("Final State")
    printQueens(qBest, n)
    print("Final Num Attacks:", best)


if __name__ == "__main__":
    main()

