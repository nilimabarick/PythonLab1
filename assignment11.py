# handle divide by zero exception
# a = int(input("enter 1st number: "))
# b = int(input("enter nd number: "))
# try:
#     c = a/b
#     print("Result: ", c)
# except:
#     print("can't devide by zero...")


# handle index out-of-range exception

# my_list = [10.50,80]
# try:
#     print(my_list[5])
# except IndexError:
#     print("Index is not out of range...!")

# create and raise a custom exception

# class AgeError(Exception):
#     def __init__(self, age):
#         self.age = age
#         self.message = f"Age {age} is not allowed"
#         super().__init__(self.message)

# def check_age(age):
#     if age < 18:
#         raise AgeError(age)
#     print("access granted")

# try:
#     check_age(15)
# # except AgeError as e:
# #     print(e)


# # Bank System Using Exception Handling


# class InsufficientBalanceError(Exception):
#     pass



# class BankAccount:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         try:
#             if amount <= 0:
#                 raise ValueError("Deposit amount must be positive")
#             self.balance += amount
#             print("Deposited:", amount)
#         except ValueError as e:
#             print("Error:", e)

#     def withdraw(self, amount):
#         try:
#             if amount <= 0:
#                 raise ValueError("Withdrawal amount must be positive")
#             if amount > self.balance:
#                 raise InsufficientBalanceError("Insufficient balance!")
#             self.balance -= amount
#             print("Withdrawn:", amount)
#         except ValueError as e:
#             print("Error:", e)
#         except InsufficientBalanceError as e:
#             print("Error:", e)

#     def check_balance(self):
#         print("Current Balance:", self.balance)



# try:
#     name = input("Enter account holder name: ")
#     acc = BankAccount(name, 1000)   

#     while True:
#         print("\n1.Deposit  2.Withdraw  3.Check Balance  4.Exit")
#         choice = int(input("Enter choice: "))

#         if choice == 1:
#             amount = float(input("Enter amount: "))
#             acc.deposit(amount)

#         elif choice == 2:
#             amount = float(input("Enter amount: "))
#             acc.withdraw(amount)

#         elif choice == 3:
#             acc.check_balance()

#         elif choice == 4:
#             print("Thank you!")
#             break

#         else:
#             print("Invalid choice!")

# except ValueError:
#     print("Invalid input! Please enter numbers only.")

# except Exception as e:
#     print("Unexpected error:", e)



# progarm handling multiple exception

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     result = num1 / num2

#     my_list = [10, 20, 30]
#     print("List element:", my_list[5])

#     print("Result:", result)

# except ValueError:
#     print("Error: Please enter numbers only.")

# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")

# except IndexError:
#     print("Error: List index out of range.")

# except Exception as e:
#     print("Unexpected error:", e)

# finally:
#     print("Program execution completed.")

# File Handling Program With Proper Excdeptin Handling


try:
    
    file = open("sample.txt", "r")

    
    content = file.read()

    
    print("File Content:")
    print(content)

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Unexpected error:", e)

finally:
    
    try:
        file.close()
        print("File closed successfully.")
    except:
        pass
       


