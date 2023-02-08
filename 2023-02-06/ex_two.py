dic_one={1:10, 2:20}
dic_two={3:30, 4:40}
dic_three={5:50,6:60}

dic_four= {}
dic_four.update(dic_one)
dic_four.update(dic_two)
dic_four.update(dic_three)
print(dic_four)

#dic_five = {}

dic_five = dic_one | dic_two | dic_three

print(dic_five)