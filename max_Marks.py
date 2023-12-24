a= input("Enter the list of marks").split()
for n in range(0,len(a)):
    a[n]=int(a[n])

print(max(a))
