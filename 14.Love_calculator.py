print("Welcome to the Love Calculator!")
name1=input("1st Person Name: ")
name2=input("2nd Person name: ")

name1_lower=name1.lower()
name2_lower=name2.lower()

T= name1_lower.count("t")+name2_lower.count("t")
R= name1_lower.count("r")+name2_lower.count("r")
U= name1_lower.count("u")+name2_lower.count("u")
E= name1_lower.count("e")+name2_lower.count("e")

L= name1_lower.count("l")+name2_lower.count("l")
O= name1_lower.count("o")+name2_lower.count("o")
V= name1_lower.count("v")+name2_lower.count("v")
E= name1_lower.count("e")+name2_lower.count("e")

print(f"T: {T}"
print(f"R: {R}")
print(f"U: {U}")
print(f"E: {E}")
print(f"L: {L}")
print(f"O: {O}")
print(f"V: {V}")
print(f"E: {E}")

tt=T+R+U+E
ll=L+O+V+E

print("Your Love Score is: "+str(tt)+str(ll))