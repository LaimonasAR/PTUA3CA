from utilitybelt import change_charset 


your_text = input("Enter text in english: ")

origspace = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
keyspace  = "abcd3fgh1jklmnopqr57uvwxyz 4BCD3FGH1JKLMN0PQR57UVWXYZ"

print(change_charset(your_text,origspace, keyspace))
