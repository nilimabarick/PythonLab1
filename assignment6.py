# create a dictionary at least 5 key-values
student = {
    "name": "Nilima Barick",
    "age": 27,
    "address": "Howrah, Ranihati",
    "Phone_no": 9674875639,
    "hobby": "Read Bangaladesi Novel, Traveling",


}
print(student)

# search for a key in a dictionary
print(student["hobby"])

# count frequency of each charecter in a string using dictionary

str = "hello world"
freq = {}
for ch in str:
   freq[ch] = freq.get(ch,0) + 1
print(freq)


#write a program to marge two dictionaries
d1 = {"name1": "nilima abrick"}
d2 = {"name2": "indrani barick"}
marge_dic = d1 | d2
print(marge_dic)


# student marks management sysytem using idctionary
student = {
   "gita":{"networking": 76,"database":87,"system_analysis":88 },
    "puja":{"networking": 67,"database":96,"system_analysis":76 },
    "shima":{"networking": 66,"database":77,"system_analysis":85 },
    "sabita":{"networking": 81,"database":75,"system_analysis":88 },
    "monika":{"networking": 95,"database":57,"system_analysis":79 },
    "trisha":{"networking": 76,"database":67,"system_analysis":78 },
    
}
for name, marks in student.items():
    print("name: ", name)
    for subject, mark in marks.items():
      print(subject,":", mark)
    print()