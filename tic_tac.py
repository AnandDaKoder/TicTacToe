# Tic Tac Toe
# Drawing a game board (how do you stande game board state in a data structure?)
# Taking input from a user
# Using that input to update the game board
# You stande game board in a data structure
# You have a function that prints that data structure in a tic-tac-toe fandmat

  
def det_game_state(game_board):
    
    game_won = False
 
    if (game_board[0] == "X" and game_board[3] == "X" and game_board[6] == "X"):  
            game_won = True
    if (game_board[0] == "O" and game_board[3] == "O" and game_board[6] == "O"):
            game_won = True     
    if (game_board[1] == "X" and game_board[4] == "X" and game_board[7] == "X"):
            game_won = True
    if(game_board[1] == "O" and game_board[4] == "O" and game_board[7] == "O"):
            game_won = True
    if(game_board[2] == "X" and game_board[5] == "X" and game_board[8] == "X"): 
            game_won = True
    if(game_board[2] == "O" and game_board[5] == "O" and game_board[8] == "O"):
            game_won = True                   
    if(game_board[0] == "X" and game_board[1] == "X" and game_board[2] == "X"):
            game_won = True
    if(game_board[0] == "O" and game_board[1] == "O" and game_board[2] == "O"):
            game_won = True                          
    if(game_board[3] == "X" and game_board[4] == "X" and game_board[5] == "X"):
            game_won = True
    if(game_board[3] == "O" and game_board[4] == "O" and game_board[5] == "O"):
            game_won = True                           
    if(game_board[6] == "X" and game_board[7] == "X" and game_board[8] == "X"):
            game_won = True
    if(game_board[6] == "O" and game_board[7] == "O" and game_board[8] == "O"):
            game_won = True                                         
    if(game_board[0] == "X" and game_board[4] == "X" and game_board[8] == "X"):
            game_won = True
    if(game_board[0] == "O" and game_board[4] == "O" and game_board[8] == "O"):
            game_won = True                                                                                                
    if(game_board[2] == "X" and game_board[4] == "X" and game_board[6] == "X"):
            game_won = True
    if(game_board[2] == "O" and game_board[4] == "O" and game_board[6] == "O"):
            game_won = True
    
    return game_won

def print_game(game_board : list):
    
    print("|" + game_board[0] + "|" + game_board[1] + "|" + game_board[2] + "|")
    print("|" + game_board[3] + "|" + game_board[4] + "|" + game_board[5] + "|")
    print("|" + game_board[6] + "|" + game_board[7] + "|" + game_board[8] + "|")
        
game_board = [" "] *9

game_recaller = [" "] * 1

counternummy = 0
while det_game_state(game_board) != True:
    det_game_state(game_board)
    print ("enter a number 1-9, 10 to exit")
    user_input = int(input())
    if user_input not in game_recaller:
        for i in range (1,10):
        
            if i == user_input and user_input != 10 and counternummy%2 == 0 :
                game_board[i - 1] = "X"
                print ("player1 : enter a number 1-9, e to exit")
                if det_game_state(game_board) == True:
                    print ("player 1 wins UWU the NIGG")
                counternummy = counternummy + 1
                break
            elif counternummy % 2 != 0 and i == user_input and user_input != 10:
                game_board[i - 1] = "O"
                print ("player2 nigga: enter a number 1-9, e to exit")
                counternummy = counternummy + 1
                if det_game_state(game_board) == True:
                    print ("player 2 wins UWU the NIGG")
                break
    game_recaller.append(user_input)

    print_game(game_board)

