# # create a class and object in pyhton

class Friend:
     name = "Rupsa"
     age = 20

f1 = Friend()
print(f1.name)
print(f1.age)





# use constructor to initialize object data
class Student:
      def __init__(self,name, age): # this is constructor
          self.name = name
          self.age = age


student = Student("chandrani", 23)
print(student.name)
print(student.age)


 #create a class with multiple method

class Calculator:
     def add (self, a,b):
         print("Addition: ", a + b)
    
     def subtract(self,a,b):
         print("subtract: ", a - b)

     def multiply(self, a, b):
         print("multiply: ", a * b)

cal = Calculator()
cal.add(10,20)
cal.subtract(19,9)
cal.multiply(10,5)

# employee management system using class

 
class Employee:
     def __init__(self, emp_id, name, salary):
         self.emp_id = emp_id
         self.name = name
         self.salary = salary

     def display(self):
         print(self.emp_id, self.name, self.salary)


employees = []

while True:
     print("\n1. Add Employee")
     print("2. View Employee")
     print("3. Exit")

     choice = input("Enter choice: ")

     if choice == '1':
         emp_id = input("Enter Id: ")
         name = input("Enter name: ")
         salary = float(input("Enter salary: "))

         emp = Employee(emp_id, name, salary)
         employees.append(emp)

     elif choice == '2':
         for emp in employees:
             emp.display()

     elif choice == '3':
         break


   #  Bank Account Simultion Using oop
    
class BankAccount:
    def __init__(self, name, acc_num, balance = 0) :
        self.name = name
        self.acc_num = acc_num
        self.balance = balance
    

    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposite successfully.")
        else:
            print("Invalid amount")
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdraw successfully")
        else:
            print("Insufficient balance.")
        
    def check_balance(self,):
        print(f"Current balance: {self.balance}")

    def display_details(self):
        print("\n --- Account details---")
        print("Account number: ", self.acc_num)
        print("Name: ",self.name)
        print("Balance: ",self.balance)

account1 =  BankAccount("Rupsa Mondal", 186452926, 40000)
account1. display_details()
account1. deposite(2000)
account1.withdraw(23000)
account1.check_balance()
    

'''
THIS IS AN EXAMPLE OF HOW TWO OBJECTS INTERACT BUT TRY TO IMPLEMENT OF YOUR OWN VERSION 


EXAMPLE CODE 

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


class Customer:
    def __init__(self, name, account):
        self.name = name
        self.account = account  # interacting object

    def perform_transaction(self):
        print(f"{self.name} is making transactions...")
        self.account.deposit(1000)
        self.account.withdraw(500)
        print("Remaining Balance:", self.account.balance)


# Creating objects
account1 = BankAccount(2000)
customer1 = Customer("Indra", account1)

# Interaction happens here
customer1.perform_transaction()

'''

'''
ASSIGNMENT CHECKED AND UPDATED 
'''

    
