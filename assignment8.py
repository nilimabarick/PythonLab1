
# Create a File And Write Text Into It

file = open("content.txt", "w")
file.write( "The story of “Suicide Note” is actually very silent, yet deeply emotional inside.\n")
file.write("It portrays the life of a person who appears completely normal form the outside\n")
file.write("smiling, talking, and living life as usually.\n")
file.write("But deep inside, They struggle with loneliess, pain and unknown pressures.\n")
file.write("Their feeling remain unspoken, and over time those emotions comes out in the form of a NOTE!! ")
file.close()


file.close()


# Read content of a file

file = open("content.txt", "r")
content = file.read()
print(content)
file.close()


# Count number of a lines in a file
file = open("content.txt", "r")
lines = file.readlines()
count = len(lines)
print("Total number of lines: ", count)
file.close()


# copy contents from one file to onther
with open("content.txt", "r") as source:
    data = source.read()

with open("copy.txt", "w") as target:
    target.write(data)

# Find word frequency from a text file 


with open("content.txt", "r") as file:
    text = file.read()

words = text.lower().split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] +=1
    else:
        frequency[word] = 1

for word, count in frequency.items():
    print(word, ":", count)

# File based student record management system 

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    
    if choice == "1":
        roll = input("Enter Roll: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        file = open("students.txt", "a")
        file.write(roll + " " + name + " " + marks + "\n")
        file.close()

        print("Record Added")

    
    elif choice == "2":
        try:
            file = open("students.txt", "r")

            data = file.read()

            if data == "":
                print("No Records Found")
            else:
                print("\nStudent Details:")
                print(data)

            file.close()

        except FileNotFoundError:
            print("File Not Found")

    
    elif choice == "3":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")

'''
    ASSIGNMENT 8 CHECKED 
    SCORE : 10 / 10
    

'''