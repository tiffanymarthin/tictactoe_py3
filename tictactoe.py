"""
Created on Tue Nov 12 13:20:16 2019
@author: Tiffany Marthin
Tic Tac Toe 3x3 game
Milestone project #1 from Udemy Python 3 Bootcamp

"""
#Defining functions

#Display board function: display the tic tac toe board

def display_board(board):
    
    print('\n'*100) #clear the output each time the function is called

    print('      |     |')
    print('   '+board[1]+'  |  '+board[2]+'  |  '+board[3])
    print('      |     |')
    print('--------------------')
    print('      |     |')
    print('   '+board[4]+'  |  '+board[5]+'  |  '+board[6])
    print('      |     |')
    print('--------------------')
    print('      |     |')
    print('   '+board[7]+'  |  '+board[8]+'  |  '+board[9])
    print('      |     |')      

#Function to ask Player 1 to choose 'X' or 'O' marker

def player_input():  
    marker = ""
    while not(marker == 'X' or marker == 'O'):
        print('\n'*100) #clear the output each time the function is called
        marker = input("Player1: Pick a marker, X or O?").upper()
    
    if marker == 'X':
        print('Player 1 is X and Player 2 is O')
        return ['X','O','X'] #Use 3 elements to be used in alternating players
    else:
        print('Player 1 is O and Player 2 is X')
        return ['O','X','O']   

#Check the availability of the chosen position, putting a constraint of 1-9

def space_check(board, position):
    if position == 0 or position > 9 or board[position] == 'X' or board[position] == 'O':
        return False
    return True

#Ask player to pick the position in the board for their turns

def player_choice(board):
    pos_sel = False
    while (pos_sel == False):
        position_sel = input("Select number 1-9 to put your next marker (pick available position, will re-ask if unavailable):")
        pos_sel = space_check(board, int(position_sel))
    return int(position_sel)

#Modify the tic tac toe board based on player's position selection

def place_marker(board, marker, position):
    board[position] = marker
    display_board(board)

#Randomly choose which player goes first

def choose_first():

    import random

    player = 0
    player = random.randint(1,2)

    if player == 1:
        print('Player 1 plays first')
        return [0,'Current Turn - Player 1','Current Turn - Player 2']
    else:
        print('Player 2 plays first')
        return [1,'Current Turn - Player 2','Current Turn - Player 1']

#Check whether any of the player wins the game

def win_check(board, mark):
    if (board[1:4] == 3*[mark] 
    or board[4:7] == 3*[mark] 
    or board[7:] == 3*[mark] 
    or board[1:8:3] == 3*[mark] 
    or board[2:9:3] == 3*[mark] 
    or board[3::3] == 3*[mark] 
    or board[1::4] == 3*[mark] 
    or board[3:8:2] == 3*[mark]):
        return True
    else:
        return False

#Check whether the board full or not with X and O. Leaving # there because it's a placeholder for index 0

def full_board_check(board):
    if set(board) == {'X','O',"#"}:
        return True
    return False

#Ask if the players want to play again

def replay():
    yesno = ""
    while not (yesno == 'Y' or yesno == 'N'):
        yesno = input("Do you want to play again (Y/N)?").upper()
    return True if yesno == 'Y' else False 


#ACTUAL GAME LOOP
def tictactoe():
    
    gameon = True
        
    while(gameon == True):
        #initial setup of the baord, marker, and first turn
        count =  0
        initial_board = ['#','1','2','3','4','5','6','7','8','9']
        player_marker = player_input() #first player chooses the marker
        first_turn = choose_first() #randomly assigns which player goes first
        
        #loop of the actual game, alternating between 2 players and 2 markers
        for count in range(9):
            display_board(initial_board)
            if count % 2 == 0:
                print(first_turn[1])
            else:
                print(first_turn[2])

            pl_position = player_choice(initial_board) #player choosing where to put his/her marker
            
            curr_marker = player_marker[first_turn[0] + (count % 2)] #this line return which marker currently played, depending on whose turn
            
            place_marker(initial_board, curr_marker, pl_position) #if position is available, then marker is placed in the board
            
            #check each move on whether someone wins yet, or if it's a draw once the board is full
            win_i = win_check(initial_board, curr_marker)

            if win_i == True:
                print('Congrats! You win!')
                gameon = False
                break

            board_check = full_board_check(initial_board)
            if board_check == True:
                print("It's a draw!")
                gameon = False
                break
            else:
                continue

            count += 1
        
        #ask player if the they want to restart the game again
        if not replay():
            print("See you next time!")
            break

        else:
            gameon = True
            continue


tictactoe()
