#Assignment 1 Tic-Tac-Toe written by Jonathan Soderquist


def reset(): #reset the board
    board = [['1','2','3'],['4','5','6'],['7','8','9']]
    #board = [['o','x','o'],['o','x','o'],['x','o','x']]
    return board


def pturn(turn): #Switch whose turn it is and store their character
    if turn == "o":
        turn = "x"
    else:
        turn = "o"
    
    return turn


def gameOver(board): #decide if the game has ended
    game = 0 #start by assuming the game isn't over
    
    #check for a full board before the check for winners so that it doesn't replace a win
    full = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'x' or board[i][j] == 'o':
                full += 1
    if full == 9:
        game = 9

    #check up and down, left and right
    for i in range(len(board)):
        if len(set(board[i])) == 1: #check rows for 3 in a row
            game = i+1 #set where the game was won
        if len(set([board[0][i],board[1][i],board[2][i]])) == 1: #check columns for 3 in a row, the board[:][i] was just giving me board[i]
            game = 4+i

    #check diagonals
    if len(set([board[0][0],board[1][1],board[2][2]])) == 1:
            game = 7
    if len(set([board[0][2],board[1][1],board[2][0]])) == 1:
            game = 8

    #print(game)
    return game


#displays the board
def dispBoard(board):
    print("")
    print(board[0][0],"|",board[0][1],"|",board[0][2])
    print("- + - + -")
    print(board[1][0],"|",board[1][1],"|",board[1][2])
    print("- + - + -")
    print(board[2][0],"|",board[2][1],"|",board[2][2])
    print("")


def main(): #runs main part of the program
    board = reset() #set board to no xs and os
    turn = "o" #instantiate variable turn
    
    while(gameOver(board) == 0): #keep going until the game ends
        turn = pturn(turn) #switch whose turn it is
        
        dispBoard(board) #show the board
        
        choice = 0
        while int(choice) > 9 or int(choice) < 1: #keep going until they choose a space in the board
            while True:
                try: #stop the program from crashing
                    choice = int(input(turn+"'s turn to choose a square (1-9): ")) #prompt for a choice
                    break
                except:
                    print("That is not a valid input. Try again")
            if int(choice) > 9 or int(choice) < 1:
                print("That is not a valid input. Try again")


        #check to make sure the place they chose hasn't been chosen/is still a number/is less than 58 on the ascii table
        i = (choice-1)//len(board) #get whole part of division for row
        j = (choice-1)%len(board) #get the remainder for the column
        if ord(board[i][j]) < 58: #make sure they're going in an open square
            board[i][j] = turn
        else:
            print("You chose an invalid location and lost your turn") #they lose a turn if they try to cheat

    #find out who won
    game = gameOver(board)
    winner = '0'
    if game < 4:
        winner = board[game-1][0]
    elif game < 7:
        winner = board[0][game-4]
        print(game,board[0][game-4])
    elif game == 7:
        winner = board[0][0]
    elif game == 8:
        winner = board[0][2]
    
    #display who won
    dispBoard(board)
    if winner == '0':
        print("The game ended in a draw")
    else:
        print(winner,"was the winner!")

            
main() #start the game