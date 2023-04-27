import os
import sys
from datetime import datetime
import this
from this import s

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i + c)] = chr((i + 13) % 26 + c)

my_text = "".join([d.get(c, c) for c in s])
print(my_text)


def import_this(my_text):
    now = datetime.now()
    i = 0
    with open("frst.txt", "w", encoding="utf-8") as f:
        f.write(my_text)

    with open("frst.txt", "r", encoding="utf-8") as f:
        print(f.read())

    with open("frst.txt", "a", encoding="utf-8") as f:
        f.write(f"\n{str(now)}")

    # with open("frst.txt", "r", encoding="utf-8") as f:
    #     print(f.read())
    with open("frst.txt", "r", encoding="utf-8") as read_file:
        lines = read_file.readlines()
        with open("frst.txt", "w", encoding="utf-8") as write_file:
            for read_line in lines:
                i += 1
                write_file.write(f"{i}. {read_line}")

    with open("scnd.txt", "r", encoding="utf-8") as f:
        print(f.read())

    with open("scnd.txt", "w", encoding="utf-8") as f:
        f.seek(1)
        f.write("2.Gražu yra geriau nei bjauru.")

    with open("scnd.txt", "r", encoding="utf-8") as f:
        print(f.read())


# my_text = this.s
# print(my_text)
# deciphered = ""
# for c in this.s:
#     try:
#         deciphered += this.d[c]
#     except ValueError:
#         deciphered += c
# print(deciphered)

# with open("frst.txt", "w", encoding="utf-8") as f:
#     f.write(sys.stdout())
#     import this
# f = open('output.txt','w')
# sys.stdout = f
# import this

# orig_stdout = sys.stdout
# f = open("out.txt", "w")
# sys.stdout = f

# import this

# sys.stdout = orig_stdout
# f.close()
# my_text = """The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!"""
import_this(my_text=my_text)
