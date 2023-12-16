h= input("Enter your height")
w= input("Enter your weight")

bmi=int(w)/float(h) ** 2

print(int(bmi))

if bmi<18.5:
    print("Under Weight")
elif  bmi<25:
    print("Normal Weight")
elif bmi<30:
    print("Over Weight")
elif bmi<35:
    print("Obse")
elif bmi>35:
    print("Clinically Obse")
else:
    print("error")