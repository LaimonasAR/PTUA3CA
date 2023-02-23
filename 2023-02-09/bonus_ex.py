# Create a list of letters and generate 5 diferent words for 5 different lists. (A word must the size between 5 and letters)
# Then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}
# And all words sorted in one list.

#final answer dictionary  of letter count
#origspace = "a",'b","cdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import random
letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","w","x","y","z"]

#word_lenghth = random.randint(5,15)
my_dict = {}

for z in range(0,5):
    my_dict['list_'+str(z)]=[]
    #first_list = []
    for i in range(0, 5):
        word_lenghth = random.randint(5,15)
        rand_word_list = []
        for a in range(word_lenghth):
            rand_letter_number = random.randint(0,24)
            rand_letter = letter_list[rand_letter_number]
            rand_word_list.append(rand_letter)
            rand_word = ''.join(map(str,rand_word_list))
        my_dict['list_'+str(z)].append(rand_word)
   # print(my_dict['list_'+str(z)])
print(my_dict)

# for keys, lists in my_dict.items():
#     #print(lists)
#     #keys = []
#    # print(keys)


#     for word in lists:
#         #print(word)
#         for letter in word:
#            # print(letter)
            