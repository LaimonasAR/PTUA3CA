# with open("failas.txt", 'r') as r_failas:
#     with open("failo_kopija.txt", 'w') as w_failas:
#         for r_eilute in r_failas:
#             w_failas.write(r_eilute)


with open("cat_pic.jpg", "rb") as r_failas:
    with open("cat_copy.jpg", "wb") as w_failas:
        for r_eilute in r_failas:
            w_failas.write(r_eilute)
