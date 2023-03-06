test_list = ["zero value"," "," ","X"," ","X"," ","X"," "," ",]

player_letter = "X"
def make_move(game:list):
    available_pos = ["zero value","1","2","3","4","5","6","7","8","9",]
    for pose in game:
        
        if pose != ' ':
            print(i)
            available_pos[i] = pose
            print(available_pos[i])
        else:
            available_pos[i] = available_pos[i]
        i+=1
    print(available_pos)
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
    pos_range = range(1,9)
    while pos_check is False:
        pos_input = input("Please enter the position of Your symbol: ")  
        try:
            pos_input = int(pos_input)
            if int(pos_input) in pos_range:
                letter_pos = pos_input
                pos_check = True
        except ValueError: #idek cia loginima klaidos :D 
            print("Position MUST BE integer between 1 and 9")

make_move(test_list)
make_move(test_list)
make_move(test_list)
make_move(test_list)