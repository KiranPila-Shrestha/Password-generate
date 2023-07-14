import random

chars = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&&*()")

while 1:
    len_password = int(input("Enter the length of the password: "))
    password_count= int(input("how many password do u want? : "))
    for x in range(0, password_count):
        password = ""
       
        for x in range (0, len_password):
            password_char = random.choice(chars)
            password = password + password_char
        print(password)

