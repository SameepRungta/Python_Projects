row1 = ["🪙","🪙","🪙",]
row2 = ["🪙","🪙","🪙",]
row3 = ["🪙","🪙","🪙",]

trow = [row1, row2, row3]

a = input("enter the index location using coma , : ")

i=a.split(", ")

f1=int(i[0])
f2=int(i[1])

trow[f1][f2]="🤡"

print(row1)
print(row2)
print(row3)