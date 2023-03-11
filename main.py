gameboard = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
p1sym = "X"
p2sym = "O"
player1 = True
gameGoesOn = True
bookToCol = {"a": 0, "b": 1, "c": 2}
winner = ""
lap = 0
names = False

def printField(board):
    global lap
    for i in range(20):
        print("-", end="")
    print(f"\nRound {lap}")
    print(f"  A  B  C\n1 {board[0][0]}  {board[0][1]}  {board[0][2]}\n2 {board[1][0]}  {board[1][1]}  {board[1][2]}\n3 {board[2][0]}  {board[2][1]}  {board[2][2]}")
    lap+=1

def convertInput(pos):
    global player1
    global gameboard
    global bookToCol
    global p1sym
    global p2sym
    global gameGoesOn
    if pos == "quit":
        print("Bye bye.")
        exit()
    if pos == "restart":
        for i in range(len(gameboard)):
            for j in range(len(gameboard[i])):
                gameboard[i][j] = " "
        player1 = True
        lap = 1
        print("\n")
        return (0)
    if pos == "help":
        print("Type        to\n\nrestart     clear field\nquit        end game\nhack        win\n")
        return (0)
    if pos == "hack":
        if player1:
            print("Player X wins!")
            exit()
        else:
            print("Player O wins!")
            exit()

    if len(pos) == 2:
        try:
            col = pos[1]
            col = col.lower()
            row = int(pos[0]) - 1
        except:
            col = pos[0]
            col = col.lower()
            row = int(pos[1]) - 1

        if type(col) == str and type(row) == int or type(row) == int and type(col) == str:
            try:
                col = pos[1]
                col = col.lower()
                row = int(pos[0]) - 1
                try:
                    col = bookToCol[col]
                    gameboard[row][col] = gameboard[row][col]
                except:
                    print("Index Error.")
                    return(0)
            except:
                col = pos[0]
                col = col.lower()
                row = int(pos[1]) - 1
                try:
                    col = bookToCol[col]
                    gameboard[row][col] = gameboard[row][col]
                except:
                    print("Index Error.")
                    return(0)

            if player1 and gameboard[row][col] == " ":
                gameboard[row][col] = p1sym
                player1 = False
            elif player1 != True and gameboard[row][col] == " ":
                gameboard[row][col] = p2sym
                player1 = True
            else:
                print("Already filled!\n")
        else:
            print("Invalid Input!")
            return (0)
    else:
        print("Invalid Input!")
        return (0)

def searchWinner(board):
    global winner
    # search rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            print(f"Player {board[i][0]} wins!")
            if names:
                if board[i][0] == p1sym:
                    print(f"Congrats {p1}.")
                else:
                    print(f"Congrats {p2}.")
            else:
                print("Whoever that is.")
            exit()
    # search columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != " ":
            print(f"Player {board[0][j]} wins!")
            if names:
                if board[0][j] == p1sym:
                    print(f"Congrats {p1}.")
                else:
                    print(f"Congrats {p2}.")
            else:
                print("Whoever that is.")
            exit()
    # across
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        print(f"Player {board[0][0]} wins!")
        if names:
            if board[0][0] == p1sym:
                print(f"Congrats {p1}.")
            else:
                print(f"Congrats {p2}.")
        else:
            print("Whoever that is.")
        exit()
    if board[0][2] == board[1][1] == board[2][0] and board[2][0] != " ":
        print(f"Player {board[0][2]} wins!")
        if names:
            if board[0][2] == p1sym:
                print(f"Congrats {p1}.")
            else:
                print(f"Congrats {p2}.")
        else:
            print("Whoever that is.")
        exit()

def checkend(board):
    counter = 0
    for row in board:
        for cell in row:
            if cell != " ":
                counter+=1
    if counter == 9:
        print("Tie!")
        exit()

choice = input("Wanna play with your names? [yes/no]: ")
choice = str(choice)
if choice == "yes":
    p1 = input("Player 1's name: ")
    p2 = input("Player 2's name: ")
    print("Names set. Have fun playing!\n")
    names = True
else:
    print("No names? Ok, have fun playing!\n")

print("Type help to show the manual.\n")
printField(gameboard)
while gameGoesOn:
    position = input("Input: ")
    convertInput(position)
    printField(gameboard)
    searchWinner(gameboard)
    checkend(gameboard)