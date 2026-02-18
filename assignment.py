# check number is positive or negative
num1 = int(input("eneter num1: "))
if(num1>0):
    if(num1 == 0):
        print("you enterd 0")
    print("number is positive")
else:
    print("number is negetive")
# check number is even or odd
if(num1 % 2 == 0):
    print("number is even number") 
else:
    print("number is odd number") 
# find the greatest of three number 
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))
if(num1>num2 & num1>num3):
    print("num1 is grater")
elif(num2>num1 & num2>num3):
    print("num2 is grater")
else:
    print("num3 is grater")
# calculate electricity bill using condition
# uo to 50 units 5
# up to 51 to 150 units 10
# up to 151 to 250 untis 20

unit = int(input("enter units: "))
if(unit<= 50):
    bill= unit * 5
    print("your bill: ", bill)
elif(unit<=150):
    bill =(( 10 * (unit - 50)))
    print("your bill : ", bill)
elif(unit <= 250):
    bill = (20 * (unit - 150))
    print("your bill: ", bill)
else:
    print("invalid choice")
# year is leap year or not
year = int(input("enter year : ")) 
if(year%4==0 and year% 100 !=0 or year%400==0):
    print("leap year")
else:
    print("not leap year")
# calculate student grade
marks = int(input("enter total marks: "))
if(marks<=500 and marks >=400 ):
  print("your grade A")
elif(marks<=400 and marks>=300):
    print("your grade B")
elif(marks>300 and marks<=200):
    print("your grade C")
else:
    print("you are fail or invalid number")

'''
REMARKS: 

    1. OVERALL EVERYTHING IS OKAY 
    2. GRADE CHECKING CODE MUST ALSO INCLUDE A RANGE OF 600 - 700
    3. DO ADD SPACES IN THE INPUT BOX WHEN PROMPTING FOR INPUTS

FINAL SCORE: 9 / 10
'''