
def calculate_bmi(height,weight):

    print("Height = " , height)
    print("Weight = " , weight)
#calculate_bmi(weight=57, height=1.73)

#weight=float(input("your weight : "))
#height=float(input("your height: "))

#weight=70
#height=1.73
    
    bmi= (weight/height/height)*10000
   
    print("Your BMI is ", bmi)

    if(bmi<18.5):
        print("-1")
    elif((bmi<=25.0) and (bmi>=18.5)):
        print("0")
    else:
         print("1")


def main():
    a=int(input('enter height in cm ONLY: '))
    b=int(input('enter weight in kg ONLY: '))
    calculate_bmi(a,b)


if __name__ == "__main__":              # for the main function to work
    main()