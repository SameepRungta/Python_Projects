bill=input("Welcome to the tip Calculator/nWhat was the total bill? $")
tip=input("What percentage tip would you like to give? 10, 12, or 15? ")
pep=input("How many people to split the bill? ")

perc=float(bill)*float(tip)/100
tt=float(bill)+perc
split=float(tt)/int(pep)

print(f"Each person should pay: ${round(split,2)}")

