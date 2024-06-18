weight=int(input("Enter your weight in Kg: "))
print("\n Please Select and option for entering height: ")
print("Option 1. Centimeter")
print("Option 2. Feet \n")

option = input("Enter your choice 1 Or 2: ")
if option == '1':
    height=int(input(print("Enter your height in cm: ")))
    h=height*0.01
    H=h*h
    bmi= weight/H
    print("\n Your BMI is: ", bmi)
    if bmi>=25:
        print("\n Category: You are overweight.")
    elif 18.5< bmi >24.9:
        print("\n Category: You are healthy.")
    else:
        print("\n Category: You are under weight.")
else:
    height=float(input(print("Enter your height in ft: ")))
    h=height*0.305
    H=h*h
    bmi= weight/H
    print("\n Your BMI is: ", bmi)
    if bmi>=25:
        print("\n Category: You are overweight.")
    elif 18.5> bmi <24.9:
        print("\n Category: You are healthy.")
    else:
        print("\n Category: You are under weight.")
