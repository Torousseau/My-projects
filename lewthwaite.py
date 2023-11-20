def newBoard(n):
    board = [[" " for i in range(n)] for i in range(n)]
    player = 2
    for i in range(n):
        for j in range(n):
            board[i][j] = player
            player = (player % 2) + 1
    board[n // 2][n // 2] = 0
    return board


def displayBoard(board, n):
    for i in range(n):
        print(i + 1, end=" | ")
        for j in range(n):
            if board[i][j] == 1:
                print("x", end=" ")
            elif board[i][j] == 2:
                print("o", end=" ")
            else:
                print(".", end=" ")
        print()
    print("   ", end=" ")
    for k in range(n):
        print("_", end=" ")
    print()
    print("   ", end=" ")
    for l in range(n):
        print(l + 1, end=" ")
    print()


def possiblePawn(board, n, player, i, j):
    return (0 <= i <= n and 0 <= j <= n and board[i][j] == player and
            ((i < n - 1 and board[i + 1][j] == 0)
             or (j < n - 1 and board[i][j + 1] == 0)
             or (i > 0 and board[i - 1][j] == 0)
             or (j > 0 and board[i][j - 1] == 0)))


def selectPawn(board, n, player):
    choice = ((int(input("Choose a line :")) - 1), (int(input("Choose a column : ")) - 1))
    while not possiblePawn(board, n, player, choice[0], choice[1]):
        choice = ((int(input("Choose a line :")) - 1), (int(input("Choose a column : ")) - 1))
    return choice


def updateBoard(board, n, i, j):
    if i < n - 1 and board[i + 1][j] == 0:
        board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
    elif j < n - 1 and board[i][j + 1] == 0:
        board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
    elif i > 0 and board[i - 1][j] == 0:
        board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
    elif j > 0 and board[i][j - 1] == 0:
        board[i][j], board[i][j - 1] = board[i][j - 1], board[i][j]


def again(board, n, player):
    for i in range(n):
        for j in range(n):
            if possiblePawn(board, n, player, i, j):
                return True
    return False


def checkSize(n):
    for i in range(1, n + 1):
        if 4 * i + 1 == n:
            return True
    return False


def lewthwaite(n):
    if not checkSize(n):
        n = 9
    board = newBoard(n)
    player = 1
    while again(board, n, player):
        displayBoard(board, n)
        print("Player ", player)
        i, j = selectPawn(board, n, player)
        updateBoard(board, n, i, j)
        player = (player % 2) + 1
    displayBoard(board, n)
    print("Winner : {} ".format((player % 2) + 1))


taille = int(input("Quelle taille voulez-vous pour votre plateau ? : "))
lewthwaite(taille)
