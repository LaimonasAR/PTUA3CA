def magic_number(number):
    # sum = 0
    if number < 1:
        return 0
    else:
        return number // 10 ** (len(str(number)) - 1) + magic_number(
            number
            - ((number // 10 ** (len(str(number)) - 1)) * 10 ** (len(str(number)) - 1))
        )


def magic_magic_number(number):
    if magic_number(number) < 1:
        return 0
    else:
        return magic_number(number) // 10 ** (
            len(str(magic_number(number))) - 1
        ) + magic_number(
            magic_number(number)
            - (
                (magic_number(number) // 10 ** (len(str(magic_number(number))) - 1))
                * 10 ** (len(str(magic_number(number))) - 1)
            )
        )


number_to_test = magic_magic_number(55845)
# print(magic_magic_number(5656555))
if number_to_test == 1:
    print("It's magic, baby")
else:
    print("Not magic :(")
