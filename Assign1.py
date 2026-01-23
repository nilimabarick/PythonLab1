# print name and age

name = input("enter your name: ")
age = int(input("enter your age: "))
print("my name is :", name)
print("my age is :", age)

# take two number and print sum, differnt, product,quotient
num1 = int(input("enter 1st number: "))
num2 = int(input("enter 2nd number: "))
sum = num1 + num2
different = num1 - num2
product = num1 * num2
quotient = num1 // num2

print("sum of two number is :", sum)
print("different of two number is :", different)
print("product os two number is :", product)
print("quotient of two number is :", quotient)


# convert tempareture celcious to fahrenhite

celcious = int(input("enter celcious"))
fahrenheit = (celcious * 9/5) + 32
print("tempareture in fahrenheit :", fahrenheit)

# create simple calculator using user input

a = int(input("enter 1st num :"))
sign = input("enter a sign :")
b = int(input("enter 2nd num :"))

if sign == '+':
    print("your result is :",str(a + b)) 
elif sign == '-':
    print("your result is :",str (a-b))
elif sign == '*':
    print("your result is :",str(a*b))
elif sign == '/':
    print("your result is :",str(a/b))
else:
    print("no sign are match")
    



# swap two number using third variable

no1 = int(input("enter 1st number :"))
no2 = int(input("enter 2nd no"))
temp = no1
no1 = no2
no2 = temp
print("after swap no1 is :", no1)
print("after swap no2 is :", no2)

# print formatted bio using input value

''' name and age already taken at the top so we dont need
    to overwrite variables so we dont need any new variable..
'''

#name = input("enter your name:")
#age = int(input("enter your age :"))

address = input("enter your address : ")
phone_no  = int(input("enter your phone no : "))
e_mail = input("enter your gamil :")
qualification = input("enter your qualification : ")
experience = input("enter your working experience: ")
language = input ("enter language to you know: ")

print("name :",name)
print("age :",age)
print("address :",address)
print("phone_no :",phone_no)
print("e_mail :",e_mail)
print("qualification :",qualification)
print("language :",language)
print("experience :",experience)

'''
note : 
  Overall it's ok. but try not use same variables for same purpose for
  example u take name and age two times when you already have them
  in the beginning of your file. 
  do remember that. 

comment:

i made some edits to look the code more readable and visuale appealing . 
also do added the spaces in the input box with colon's. 

marks:

10 / 10

status:
assignment 1 submitted and checked. 
'''
