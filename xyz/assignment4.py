# sum of two number using function
def sum(a,b):
    sum = a + b
    print(sum)
    return sum
sum (9,5)

# factorial number using function
def fact(n):
    fact = 1
    for i in range(1, n+1):
     fact *= i
    print(fact)
    return fact
    
fact(5)

#prime number using function
def prime(n):
   count = 0
   for i in range(1,n+1):
      if n % i == 0:
         count += 1
    
   if(count == 2):
        print(n,"the given umber is prime")
   else:
          print(n,"the given number is not prime")

prime(13)


#armstrong number using function
def arm(n):
   arm = 0
   c = n
   while (n > 0):
      r = n % 10
      arm = (r * r * r) + arm
      n = n // 10

   if(c == arm):
    print("armstrong number")
   else:
        print("not an armstrong number")
arm(153)      

# fibonacci series 
def fibo(n):
    a = 0
    b = 1
    for i in range(1, n):
        c = a + b
        a = b
        b = c
        print(c)
fibo(8)

# menu driven program
balance = 2000
def depo():
    global balance
    amount = int(input("the the amount to deposite: "))
    balance += amount
    print("your balance is deposite")
    print("current balance: ", balance)

def withdraw():
    global balance
    amount = int(input("enter the amount to withdraw: "))
    if amount<= balance:
        balance -= amount
        print("amount withdraw successfully")
    else:
        print("insufficient balance")

def check_balance():
    print("current balance: ", balance)

while True:
    print("1. deposite")
    print("2. withdraw")
    print("3. check balance")
    print("4. exit")

    choice = int(input("enter your choice: "))
    if choice == 1:
        depo()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        check_balance()
    elif choice == 4:
        print("thank you for using bank system")
        break
    else:
        print("invalid choice! please try again")