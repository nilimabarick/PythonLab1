user_input = int(input("enter user input for row & coloumn: "))

for i in range(user_input):
    for j in range(i+1):
        print("*", end=" ")
    print()

for i in range(user_input):
    for j in range(5 - i):
            print(" ", end="")
    for k in range(2 * i - 1):
            print("*", end="")
    print()
print()

for i in range(user_input,0, -1):
    for j in range(i):
            print("*", end=" ")
    print()