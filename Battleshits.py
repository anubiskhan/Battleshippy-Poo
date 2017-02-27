from random import randint

board = []
print "Let's play Battleship!"
while True:
    size_input = str(raw_input("What size board would you like? (S, M, L):"))
    
    if size_input == 'S':
        board_size = 5
        ships_in_play = 2
        game_length = 4
        break
    elif size_input == 'M':
        board_size = 7
        ships_in_play = 5
        game_length = 10
        break
    elif size_input == 'L':
        board_size = 9
        ships_in_play = 8
        game_length = 16
        break
    else:
        print "Please type S, M or L."
    
for x in range(board_size):
    board.append(["O"] * board_size)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_locations = []
guard = 0
ships_placed = 0
while True:
    if ships_placed == ships_in_play:
        break
    ship_row = random_row(board)
    ship_col = random_col(board)
    # print ship_col, ship_row
    for coordinates in ship_locations:
        if ship_row == coordinates[0] and ship_col == coordinates[1]:
            guard = 1
    if guard == 1:
        print "Not adding"
        guard = 0
    else:
        ships_placed = ships_placed + 1
        ship_locations.append([ship_row,ship_col])
    

# print ship_locations

hit_counter = 0
for turn in range(game_length):
    print "There are " + str(ships_placed - hit_counter) + " ships on he board."
    if turn == game_length:
        print "Game Over"
        break
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    guess_row = guess_row - 1
    guess_col = guess_col - 1


    if (guess_row < 0 or guess_row > board_size) or (guess_col < 0 or guess_col > board_size):
        print "Oops, that's not even in the ocean."
        continue
    elif(board[guess_row][guess_col] == "X"):
        print "You guessed that one already."
    hit_guard = 0        
    for coordinates in ship_locations:
        if guess_row == coordinates[0] and guess_col == coordinates[1]:
            hit_guard = 1
            print "Congratulations! You sunk a battleship!"
            board[guess_row][guess_col] = "B"
            hit_counter = hit_counter + 1
            if hit_counter == ships_in_play:
                print "G fucking G, mate!"
                break
    if hit_guard == 0:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
    print_board(board)





