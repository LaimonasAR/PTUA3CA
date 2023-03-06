




def game_board(game):

    print(game[1] + '|' + game[2] + '|' + game[3])
    print('-+-+-')
    print(game[4] + '|' + game[5] + '|' + game[6])
    print('-+-+-')
    print(game[7] + '|' + game[8] + '|' + game[9])

def check_x(game_step_x: list) -> bool:
    x_won = False
    x_wins = [
        ["zero value","X","X","X"," "," "," "," "," "," ",],
        ["zero value"," "," "," ","X","X","X"," "," "," ",],
        ["zero value"," "," "," "," "," "," ","X","X","X",],
        ["zero value","X"," "," ","X"," "," ","X"," "," ",],
        ["zero value"," ","X"," "," ","X"," "," ","X"," ",],
        ["zero value"," "," ","X"," "," ","X"," "," ","X",],
        ["zero value","X"," "," "," ","X"," "," "," ","X",],
        ["zero value"," "," ","X"," ","X"," ","X"," "," ",]
    ]
    for i in x_wins:
        if i == game_step_x:
            x_won = True
    return x_won

def check_o(game_step_o: list) -> bool:
    o_won = False
    o_wins = [
        ["zero value","O","O","O"," "," "," "," "," "," ",],
        ["zero value"," "," "," ","O","O","O"," "," "," ",],
        ["zero value"," "," "," "," "," "," ","O","O","O",],
        ["zero value","O"," "," ","O"," "," ","O"," "," ",],
        ["zero value"," ","O"," "," ","O"," "," ","O"," ",],
        ["zero value"," "," ","O"," "," ","O"," "," ","O",],
        ["zero value","O"," "," "," ","O"," "," "," ","O",],
        ["zero value"," "," ","O"," ","O"," ","O"," "," ",]
    ]
    for i in o_wins:
        if i == game_step_o:
            o_won = True
    return o_won

def choose_your_letter():
    
    letter_check = False
    while letter_check is False:
        letter_input = input("Please choose letter X or letter O as your symbol: ")   
        if letter_input.upper() in ("X", "O"):
            letter_input = letter_input.upper()
            letter_check = True
    if letter_input == "X":
        player_letter = "X"
        ai_letter = "O"
    else:
        player_letter = "O"
        ai_letter = "X"
    return player_letter, ai_letter




test_list = ["zero value"," "," ","X"," ","X"," ","X"," "," ",]
 
def make_move(game:list, moves_list:list):
    available_pos = ["zero value","1","2","3","4","5","6","7","8","9",]
    i=0
    for pose in game:
        if pose != ' ':
            available_pos[i] = pose
        else:
            available_pos[i] = available_pos[i]
        i+=1
    print("position table")
    # print('1' + '|' + '2' + '|' + '3')
    # print('-+-+-')
    # print('4' + '|' + '5' + '|' + '6')
    # print('-+-+-')
    # print('7' + '|' + '8' + '|' + '9')
    print(available_pos[1] + '|' + available_pos[2] + '|' + available_pos[3])
    print('-+-+-')
    print(available_pos[4] + '|' + available_pos[5] + '|' + available_pos[6])
    print('-+-+-')
    print(available_pos[7] + '|' + available_pos[8] + '|' + available_pos[9])
    pos_check = False
    pos_range = range(1,10)
    while pos_check is False:
        pos_input = input("Please enter the position of Your symbol: ")  
        try:
            pos_input = int(pos_input)
            if int(pos_input) in pos_range:
                letter_pos = pos_input
                pos_check = True
        except ValueError: #idek cia loginima klaidos :D 
            print("Position MUST BE integer between 1 and 9")
    moves_list.remove(letter_pos)
    return letter_pos

def player_move(game:list, player_letter: str, moves_list):
    position = make_move(game, moves_list)
    game[position] = player_letter

# def ai_move(game:list, ai_letter):
#     #check winning moves, make decisions
#     game[position] = ai_letter


def check_if_player_won(game:list, letter:str)-> bool:
    if letter == "X":
        if check_x(game) == True:
            return True
        else:
            return False
    elif letter == "O":   
        if check_o(game) == True:
            return True
        else:
            return False
    


def main():
    print("Hello and welcome to the GAME!")
    game = ["zero value"," "," "," "," "," "," "," "," "," ",]
    moves_list = [0,1,2,3,4,5,6,7,8,9]
    game_over = False
    while not game_over:
        game_board(game) #this prints game board

        player_letter, ai_letter = choose_your_letter()
        print(f"Your symbol is {player_letter}, computer's symbol is {ai_letter}")
        player_move(game, player_letter, moves_list)
        print(moves_list)
        game_board(game)

   # print(player_letter, ai_letter)


    # ai_letter = "O"



main()