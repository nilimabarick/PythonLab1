#sentance = input("enter a text: ")

#sentence = sentance.strip().lower()

#count_a = sentance.count('a')

#pos_is = sentance.find("is")

#sentance = sentance.replace("bad", "good")

#print(sentance.title())
#print("final sentance",sentance.title())
#print("number of times a appeard: ", count_a)
#print("the index of is: ", pos_is)

username = input("enter you username: ")

username = username.strip().lower()

count_underscore = username.count('_')

pos_find = username.find("@")

pos_index = username.index("@")

new_username = username.replace("admin", "user")

print("username in uppercase: ", new_username.upper())
print("username in titlecase: " ,new_username.title())

print("number of times underscore appears: ", count_underscore)
print("position of @ using find: ", pos_find)
print("position of @ using index: ", pos_index)