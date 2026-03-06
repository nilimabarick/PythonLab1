#TASK1 - sum of natural numbers using while loop
#n = int(input("Enter the number: "))

#sum_of_all = 0

#i = 1
#while(i<n):
    #sum_of_all += i
#    i += 1
#print(f"The sum of all value upto {n} is : ", sum_of_all)

#TASK2 - identify the smallest number using while loop

#smallest_num = 99999
#count = int(input("how many inputs: "))

#i = 0 
#while (i < count):
    #n = int(input("enter the numbers: "))

    #if smallest_num > n:
        #smallest_num = n

    #i += 1
#print("the smallest num is : ", smallest_num)
#TASK3 - passward checker using while loop

#correct_passward = 11111
#count = 1

#while True:
    #n = int(input("enter your passward : "))
    #if count == 5:
        #print("you have reached maximum number of trails!..")
        #print("please try again later!")
        #break

    #if correct_passward != n:
        #count += 1
        #print("try again!")

    #else:
       # print("access granted!")
       # break
#TASK4 - number guessing gaming using break and while

#import random

#secrect_number = random.randint(1, 50)

#print("Wellcome to the number guessing game!")
#print("Guess a number between 1 to 50!")

#while True:
    #n = int (input("Enter your guess....:"))

    #if n < secrect_number:
        #print("too low ! Try again...!")
   # elif n > secrect_number:
        #print("too big ! Try again...!")
    #else:
       ## print("yay! you have got the answer...")
        #break
#TASK5 - VIP entry game

#while True :
    #code = int (input("please enter your code: "))

    #if code % 5 != 0:
      #print("you are not a VIP !")
      #print("get away...")
    #else:
       #print("Granted access..")
       #break
#TASK6 - mario brother wooden forest lost game function


    


