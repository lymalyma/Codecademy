# Things to add: 
# Make multiple battleships: Be careful not to add battleships on top of each other
# Make it a two player game. 
# Make a bigger grid. 
# Make battleships of different sizes
# Make rematches and statistics. 

from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def create_battleship(board):
    row = random_row(board)
    col = random_col(board)
    battleship = [row, col]
    return battleship

def ship_compare(ship1, ship2):
    return ship1[0] == ship2[0] or ship1[1] == ship2[1]
        
def hit(ship, guess_row, guess_col):
    return ship[0] == guess_row and ship[1] == guess_col




#ship_row = random_row(board)
#ship_col = random_col(board)



#we're going to create 2 battleships
ship1 = create_battleship(board)
ship2 = create_battleship(board)
comparison = ship_compare(ship1, ship2)
while (comparison == True):
    ship2 = create_battleship(board)
    comparison = ship_compare(ship1, ship2)
print ship1
print ship2


for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    
    if hit(ship1, guess_row, guess_col) or hit(ship2, guess_row, guess_col):
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"

        turns_left = 4 - (turn + 1)    
        print "You have %s turns left" % (turns_left)

        print_board(board)
        if turn == 3:
            print "Game Over"
            print "The ship was at row %s and column %s" %(ship_row, ship_col)
            print "Thanks for playing!"    
        


