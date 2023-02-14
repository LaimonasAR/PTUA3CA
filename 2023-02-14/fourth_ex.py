my_string = input("Enter your string: ")
#result_string = ""

def unique_string(uni_str: str) -> str:
    result_string = ""
    string_list = uni_str.split(' ')
    for string in string_list:
        if len(string) == len(set(string)):
            result_string = result_string + " " + string
    return result_string

result = unique_string(my_string)

print(result)