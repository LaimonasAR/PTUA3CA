my_pin = input("Enter Your PIN: ")

pin_list = []
pin_list.extend(my_pin)
print(pin_list)
check_list = []
for item in pin_list:
    item = int(item)
    check_list.append(item)
#pin_code = []
#pin_code.extend(pin_list)
print(check_list)
#print(pin_code)

crack_list = [0, 0, 0, 0]

gotcha = False

while gotcha is False:

    if (crack_list==check_list):
        print("Gotcha! Your pin is: ")
        print(crack_list)
        gotcha = True
        break
    for a in range(10):
        crack_list[0] = a
        if (crack_list==check_list):
            print("Gotcha! Your pin is: ")
            print(crack_list)
            gotcha = True
            break
        for b in range(10):
            crack_list[1] = b
            if (crack_list==check_list):
                print("Gotcha! Your pin is: ")
                print(crack_list)
                gotcha = True
                break
            for c in range(10):
                crack_list[2] = c
                if (crack_list==check_list):
                    print("Gotcha! Your pin is: ")
                    print(crack_list)
                    gotcha = True
                    break
                for d in range(10):
                    crack_list[3] = d
                    #print(crack_list)
                    if (crack_list==check_list):
                        print("Gotcha! Your pin is: ")
                        print(crack_list)
                        gotcha = True
                        break
                    else:
                        print(crack_list)
                    # else:
                    #     continues