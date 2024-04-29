
def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
calculate_bmi(weight=57, height=1.73)


#weight=float(input("your weight: "))
#height=float(input("your height: "))


weight=70
height=1.73
bmi= weight/(height*height)
print("Your BMI is ", bmi)
if(bmi<18.5):
    print("Underweight")
elif((bmi<=25.0) and (bmi>=18.5)):
    print("Normal Weight")
else:
    print("overweight")