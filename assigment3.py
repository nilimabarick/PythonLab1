# print number form 1 to 10
for i in range(1,10):
    print(i)
# find factorial number of a number
no = 5
fact = 1
while(no > 1):
    fact = fact * no
    no = no - 1
    print(fact)

# print multiplication table of a number


n = int(input("enter the number: "))
i = 1
while(i<=10):
    print(n*i)
    i +=1


# check weather a number is prime 
n = int(input("enter a number to check prime nukmber: "))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count += 1
        
if(count == 2):
    print(n,"the given number is prime")
else:
    print(n,"not prime number")

# generate fibonacci series


first = 0 
second = 1
third = 0
for i in range(0,n,1):
    print(third)
    first = second
    second = third
    third = first + second


# reverse a number using loop
rev = 0
while(n>0):
    rem = n%10
    rev = (rev*10)+rem
    n = n//10
    print("reverse is: ",rev)
    




    