h_cm=int(input("Enter your height in cm: "))
w=int(input("Enter your weight in kg: "))
h_m=h_cm/100
bmi=w/h_m**2
if bmi<16:
    print("severely underweight")
elif bmi<18.5:
    print("underweight")
elif bmi<25:
    print("normal")
elif bmi<30:
    print("overweight")
else: print("obese")