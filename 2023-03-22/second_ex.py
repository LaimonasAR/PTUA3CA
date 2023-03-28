# write a function that accepts an encoded string as a parameter. This string will contain a first name, last name, and an id.
# Values in the string can be separated by any number of zeros. The id is a numeric value but will contain no zeros.
# The function should parse the string and return a Python dictionary that contains the first name, last name, and id values.
# An example input would be “Robert000Smith000123”. The function should return the following using that input:
# { “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }


def my_func(enc_str: str):
    list_one = enc_str.split("0")
    list_two = []
    # print(list_one)
    for i, element in enumerate(list_one):
        if len(element) != 0:
            list_two.append(element)
    # print(list_two)
    my_dict = {"first_name": list_two[0], "last_name": list_two[1], "id": list_two[2]}
    #my_dict = dict(zip(two lists)) butu buve geriau
    print(my_dict)


my_func("Laimonas00000Paura00000558536")
