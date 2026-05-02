# reverse a sting
text = " hii i like to learn pyhton"
print(text[::-1])

# check weather a string s palindrome

str = "madam"
if str == str[::-1]:
   print("string is palindrome")
else:
    print("string is not a palindrome")



# count vowles and consonent in a stoing
vowles = "aeiouAEIOU"
v_count = 0
c_count = 0

for char in text:
    if char in vowles:
        v_count +=1
    else:
      c_count +=1
print("the number of vowles: ", v_count)
print("the number of consonent: ", c_count)  


# remove duplicate of a stinge
new = ""
for i in text:
    if i not in new:
        new = new+i
print("new string is: ",new)

# check whether two sting are anagrams
str1 = "Race"
str2 = "Care"
str1 = str1.lower()
str2 = str2.lower()

if(len(str1) == len(str2)):

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if(sorted_str1 == sorted_str2):
        print(str1  +  "and"  + str2 +  "are anagrams")
    else:
        print(str1 + "and" + str2 + "are not anagrams")
else:
    print(str1 + "and" + str2 + "are not anagrams.")


'''
CHECKED AND COMPLETED

'''

