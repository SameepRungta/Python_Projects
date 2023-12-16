print("Welcome to Leap year Checker!")
d = input("Enter a Year")
y=float(d)
if y%4==0:
    if y%100==0:
        print("It's a Leap Year")
    else:
        if y%400==0:
            print("It's a Leap Year")
        else:
            print("It's not a Leap Year")        
else:
    print("It's Not A leap Year")        
 