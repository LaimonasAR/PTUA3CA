import random




def game_board(game):

    print(game[1] + '|' + game[2] + '|' + game[3])
    print('-+-+-')
    print(game[4] + '|' + game[5] + '|' + game[6])
    print('-+-+-')
    print(game[7] + '|' + game[8] + '|' + game[9])

# def check_x(game_step_x: list) -> bool:
#     x_won = False
#     x_wins = [
#         [" ","X","X","X"," "," "," "," "," "," ",],
#         [" "," "," "," ","X","X","X"," "," "," ",],
#         [" "," "," "," "," "," "," ","X","X","X",],
#         [" ","X"," "," ","X"," "," ","X"," "," ",],
#         [" "," ","X"," "," ","X"," "," ","X"," ",],
#         [" "," "," ","X"," "," ","X"," "," ","X",],
#         [" ","X"," "," "," ","X"," "," "," ","X",],
#         [" "," "," ","X"," ","X"," ","X"," "," ",]
#     ]
#     for i in x_wins:
#        # print(game_step_x)
#         if i == game_step_x:
#             x_won = True
#             print("X WINS")
#     return x_won

# def check_o(game_step_o: list) -> bool:
#     o_won = False
#     o_wins = [
#         [" ","O","O","O"," "," "," "," "," "," ",],
#         [" "," "," "," ","O","O","O"," "," "," ",],
#         [" "," "," "," "," "," "," ","O","O","O",],
#         [" ","O"," "," ","O"," "," ","O"," "," ",],
#         [" "," ","O"," "," ","O"," "," ","O"," ",],
#         [" "," "," ","O"," "," ","O"," "," ","O",],
#         [" ","O"," "," "," ","O"," "," "," ","O",],
#         [" "," "," ","O"," ","O"," ","O"," "," ",]
#     ]
#     for i in o_wins:
#         if i == game_step_o:
#             o_won = True
#     return o_won

def checking(game: list, letter:str) -> bool:
    if (
        (game[1] == letter and game[2] == letter and game[3] == letter) or
        (game[4] == letter and game[5] == letter and game[6] == letter) or
        (game[7] == letter and game[8] == letter and game[9] == letter) or
        (game[1] == letter and game[4] == letter and game[7] == letter) or
        (game[2] == letter and game[5] == letter and game[8] == letter) or
        (game[3] == letter and game[6] == letter and game[9] == letter) or
        (game[1] == letter and game[5] == letter and game[9] == letter) or
        (game[3] == letter and game[5] == letter and game[7] == letter)
    ):
        winner = True
    else:
        winner = False
    return winner

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

 
def make_move(game:list, moves_list:list):
    available_pos = [" ","1","2","3","4","5","6","7","8","9",]
    i=0
    for pose in game:
        if pose != ' ':
            available_pos[i] = pose
        else:
            available_pos[i] = available_pos[i]
        i+=1
    print("position table")#this print must be skipped when computer turn
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
    #pos_range = range(1,10)
    while pos_check is False:
        pos_input = input("Please enter the position of Your symbol: ")  
        try:
            pos_input = int(pos_input)
            if int(pos_input) in moves_list:
                letter_pos = pos_input
                pos_check = True
            else:
                print("Shit, try again")
        except ValueError: #idek cia loginima klaidos :D 
            print("Position MUST BE integer between 1 and 9 and in the available moves table")
    moves_list.remove(letter_pos)
    return letter_pos

def make_list_copy(old_list):
    new_list = []
    for i in old_list:
        new_list.append(i)
    return new_list

def make_move_ai(game:list, moves_list:list, ai_letter, player_letter):
    moves_list_copy = make_list_copy(moves_list)
    win_block = False
    for move in moves_list_copy:
        #print(f"GAME IS {game}")
        testing_list = make_list_copy(game)
        testing_list_enemy = make_list_copy(game)
        testing_list[move] = ai_letter
       #print(testing_list)
        testing_list_enemy[move] = player_letter
        moves_list_copy_two = make_list_copy(moves_list_copy)
        moves_list_copy_two.remove(move)
        #print(f"TESTING list {testing_list}")
       # print(f"TESTINGLIST ENEMY {testing_list_enemy}")
        #print(moves_list_copy)
       # print(moves_list_copy_two)
        # if checking(testing_list_enemy, player_letter) is True:
        #     poing = move
        #     break
        # elif checking(testing_list, ai_letter) is True:
        #     poing = move
        #     break
        if checking(testing_list, ai_letter) is True:
            print(f"Selected winning move {move}")
            poing = move
            win_block = True
            break
        elif checking(testing_list_enemy, player_letter) is True:
            print(f"Selected blocking move {move}")
            #print(f"Enemy list  {testing_list_enemy}")
            poing = move
            win_block = True
            break
        else:
            win_block = False
            # for deeper_move in moves_list_copy:

            #     testing_list_two = make_list_copy(testing_list)
            #     moves_list_copy_two = make_list_copy(moves_list_copy)
 
            #     testing_list_two[deeper_move] = ai_letter
            #     moves_list_copy_two.remove(deeper_move)
 
            #     if checking(testing_list_two, ai_letter) is True:
            #         poing = move
            #         break
            #    # elif checking(testing_list_two)
            #     else:
            #         for even_deeper_move in moves_list_copy_two:
            #             testing_list_three = make_list_copy(testing_list_two)
            #             testing_list_three[even_deeper_move] = ai_letter
            #             if checking(testing_list_three, ai_letter) is True:
            #                 poing = move
            #                 break
    if win_block == False:
        corners = [1,3,7,9]
        sides = [2,4,6,8]
        random.shuffle(corners)
        random.shuffle(sides)
        if game[5] == " ":
            poing = 5
        elif game[5] == ai_letter:
            for pos in sides:
                if game[pos] == " " and win_block == False and game[opposite_side(pos)] != player_letter:
                    print(f"Selected random side {pos}")
                    win_block = True
                    poing = pos
                    break
        elif win_block == False:
            for pos in corners:
                if game[pos] == " " and win_block == False and game[opposite_corner(pos)] != player_letter:
                    print(f"Selected random corner {pos}")
                    win_block = True
                    poing = pos
                    break
            for pos in sides:
                if game[pos] == " " and win_block == False and game[opposite_side(pos)] != player_letter:
                    print(f"Selected random side {pos}")
                    win_block = True
                    poing = pos
                    break
        else:
            win_block = False

    if win_block == False:
        corners = [1,3,7,9]
        sides = [2,4,6,8]
        random.shuffle(corners)
        random.shuffle(sides)
        if game[5] == " ":
            poing = 5
        elif win_block == False:
            for pos in corners:
                if game[pos] == " " and win_block == False:
                    print(f"Selected random corner {pos}")
                    win_block = True
                    poing = pos
                    break
            for pos in sides:
                if game[pos] == " " and win_block == False:
                    print(f"Selected random side {pos}")
                    win_block = True
                    poing = pos
                    break
            # if testing_list[5] == " ":
            #     poing = 5
            # elif testing_list[1] == " ":
            #     poing = 1
            # elif testing_list[3] == " ":
            #     poing = 3
            # elif testing_list[7] == " ":
            #     poing = 7
            # elif testing_list[9] == " ":
            #     poing = 9
            # else:
            #     poing = random.choice([2, 4, 6, 8]) #CIA NEGERAI< TIK PATIKRINIMUI!!!
        #    continue
      
    moves_list.remove(poing)
    return poing
   #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def opposite_corner(corner):
    if corner == 1:
        op_corner = 9
    elif corner == 3:
        op_corner = 7
    elif corner == 7:
        op_corner = 3
    else:
        op_corner = 1
    return op_corner

def opposite_side(side):
    if side == 2:
        op_side = 8
    elif side == 4:
        op_side = 6
    elif side == 6:
        op_side = 4
    else:
        op_side = 2
    return op_side

def player_move(game:list, player_letter: str, moves_list):
    position = make_move(game, moves_list)
    game[position] = player_letter

def ai_move(game:list, ai_letter: str, moves_list, player_letter):
    position = make_move_ai(game, moves_list, ai_letter, player_letter)
    game[position] = ai_letter

# def ai_move(game:list, ai_letter):
#     #check winning moves, make decisions
#     game[position] = ai_letter


# def check_if_won(game:list, letter:str)-> bool:
#     if letter == "X":
#         print(game)
#         if check_x(game) == True:
#             print(game)
#             return True
#         else:
#             return False
#     elif letter == "O":   
#         if check_o(game) == True:
#             return True
#         else:
#             return False

def first_move():
    check_if_correctly_entered = False
    while check_if_correctly_entered == False:
        heads_tails = input("Let's firgure Our who goes first, enter 0 for Heads or 1 for tails: ")
        try:
            heads_tails = int(heads_tails)
            if heads_tails in (0, 1):
                check_if_correctly_entered = True
        except ValueError:
            continue
          
    flip_a_coin = random.randint(0, 1)
    print(f"Coin flips {flip_a_coin}")

    if heads_tails == flip_a_coin:
        whose_turn = "player"
        print("Correct, You go first")
    else:
        whose_turn = "ai"
        print("Inorrect, AI goes first")
    return whose_turn

def main():
    print("Hello and welcome to the GAME!")
    game = [" "," "," "," "," "," "," "," "," "," ",]
    moves_list = [1,2,3,4,5,6,7,8,9]
    game_over = False
    game_board(game) #this prints game board
    player_letter, ai_letter = choose_your_letter()
    print(f"Your symbol is {player_letter}, computer's symbol is {ai_letter}")
    whose_turn = first_move()

    while not game_over:
        if whose_turn == "player":
            player_move(game, player_letter, moves_list)
           # print(moves_list)
            game_board(game)
            if checking(game, player_letter) is True:
                print("WOO HOO")
                game_over = True
            else:
                if len(moves_list) == 0:
                    print("No one wins this time")
                    game_over = True
                    break
                else:
                    whose_turn = "ai"

        else:
            ai_move(game, ai_letter, moves_list, player_letter)
            print("AI makes a move")
            game_board(game)
            if checking(game, ai_letter):
                print("AI is smarter than YOU, it won!")
            else:
                if len(moves_list) == 0:
                    print("No one wins this time")
                    break
                else:
                    whose_turn = "player"
   # print(player_letter, ai_letter)


    # ai_letter = "O"



main()