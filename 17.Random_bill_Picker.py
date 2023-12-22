import random
a = input("Enter Multiple names using , :")
names= a.split(", ")
print(names)
print("Bill should be Pay by " + random.choice(names))