# import os
# import sys
# # print(dir(os))
# print(os.name)
# print(sys.platform)

# import os

# # os.chdir("C:\\Users\\Nekas")
# print(os.getcwd())

# print(os.listdir())

# os.makedirs("new_folder/few_nolder")
# with open("file.txt", "a") as failas:
#     failas.write("Hello, Wrold \n")

# with open("file.txt", "r") as f:
#     print(f.read())


# with open("file.txt", "a", encoding="utf-8") as failas:
#     failas.write("Čia yra failas")

# with open("file.txt", "r", encoding="utf-8") as f:
#     print(f.read())

# with open("failas.txt", "w", encoding="utf-8") as failas:
#     failas.write("Test")
#     failas.seek(0)
#     failas.write("BE")

with open("file.txt", "r", encoding="utf-8") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

with open("file.txt", "r", encoding="utf-8") as file:
    print(file.readlines())

with open("file.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
