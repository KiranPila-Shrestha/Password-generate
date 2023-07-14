import random

password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*():"
length_password = int(input("Enter the length of the password:"))
a = "".join(random.sample(password, length_password)) # random.sample is used to extract some value from which we have given  and join just join those random values.
#password is  the variables which contain the sample values and what length of password is required is written in the length_password variable.
print(f"Your password is: {a}")
