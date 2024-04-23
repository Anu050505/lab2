""" EXERSIZE 1


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
    print("overweight")"""








"""EXERSIZE 2(WITHOUT FUNCTIONS)


a=int(input("enter number: "))
b=int(input("enter number: "))
c=int(input("enter number: "))
d=int(input("enter number: "))
print(a,b,c,d)

e=a/1.0
f=b/1.0
g=c/1.0
h=d/1.0
print(e,f,g,h)


if(e>=f and e>=g and e>=h):
    print("max value is: ",e)
elif(f>=e and f>=g and f>=h):
    print("max value is: ",f) 
elif(g>=e and g>=f and g>=h):
    print("max value is: ",g) 
else:
    print("max value is: ",h) 

print("DONE")"""








"""EXERSIZE 2(WITH FUNCTION)"""


def display_main_menu():
    print("Enter some numbers separated by commas(e.g 5,67,32)")


def get_user_input():
    floatlist=[]
    inside=input()
    x=inside.split(",")
    floatlist = [float(value) for value in x]
    return floatlist

def calc_avg_temp(nu):
    average=sum(nu)/len(nu)
    print("Average is" , average)
    return average

def calc_min_max_temp(na):
    least=min(na)
    most=max(na)
    print("Max is ", most)
    print("Min is ", least)
    answer=[least,most]
    return answer
def median_id(ne):
    sorted(ne)
    if len(ne)%2==0:
        print("Even")
        answ=ne[int(len(ne)-len(ne)/2)]+ne[int(len(ne)-len(ne)/2)-1]
    else:
        answ=ne[int(len(ne)-len(ne)/2)]
        print("Odd")
    print("Median is ", answ)
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python prog")
    display_main_menu()
    numy=get_user_input()
    calc_avg_temp(numy)
    calc_min_max_temp(numy)
    median_id(numy)

if __name__ == "__main__":
    main()

   



