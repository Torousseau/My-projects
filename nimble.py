from random import randint


def newBoard(n, p):
    return [randint(0, p) for i in range(n)]


def display(board, n):
    l = [board, ["-" for x in range(n)], [x for x in range(1, n + 1)]]
    for i in range(3):
        for j in range(n):
            if l[i][j] == "-":
                print(l[i][j] * 5, end="")
            else:
                print(l[i][j], " | ", end="")
        print()


def possibleSquare(board, n, i):
    return n > i > 0 != board[i]


def selectSquare(board, n):
    choice = int(input("Choose a square : ")) - 1
    while 0 < choice < len(board) and not possibleSquare(board, n, choice):
        choice = int(input("Choose a square : ")) - 1
    return choice


def possibleDestination(board, n, i, j):
    somme = 0
    for k in range(n):
        somme += board[k]
    return board[j] != somme and j < i


def selectDestination(board, n, i):
    choice = int(input("Choose a destination : ")) - 1
    while not possibleDestination(board, n, i, choice):
        choice = int(input("Choose a destination :  ")) - 1
    return choice


def move(board, n, i, j):
    board[i] -= 1
    board[j] += 1


def lose(board, n):
    for k in range(1, n):
        if possibleSquare(board, n, k) and possibleDestination(board, n, k, k - 1):
            return True
    return False


def nimble(n, p):
    board = newBoard(n, p)
    player = 1
    while lose(board, n):
        display(board, n)
        print("Player ", player)
        i = selectSquare(board, n)
        j = selectDestination(board, n, i)
        move(board, n, i, j)
        player = (player % 2) + 1
    display(board, n)
    print("Winner : {} ".format((player % 2) + 1))


taille = int(input("Quelle taille voulez-vous pour votre plateau ? : "))
pionMax = int(input("Combien de pions voulez vous au maximum ? : "))
nimble(taille, pionMax)
