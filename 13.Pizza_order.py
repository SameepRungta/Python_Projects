print("Welcome Pizza World!")
s=input("What size you Want? S, M, L ")
p=input("Do you want pepperoni? Y or N ")
c= input("Do you want extra cheese? Y or N ")

bill=0

if s=="S":
    bill=bill+15
    if p=="Y":
        bill=bill+2
    else:
        bill=bill+0
            
elif s=="M":
    bill=bill+20
    if p=="Y":
        bill=bill+2
    else:
        bill=bill+0
elif s=="L":
    bill=bill+25
    if p=="Y":
        bill=bill+2
    else:
        bill=bill+0
else:
    bill=bill+0
    if p=="Y":
        bill=bill+0

if c=="Y":
    bill=bill+1

print(f"Amount to pay is {bill}")