#dict = {
 #   "name" : "nilima",
  #  "DOB" : "22.09.1998",
  #  "address" : "ranihati",
  #  "learning" : ["python", "C", "java"], # we can't create list as a key
  #  "topic" : ("dictionary", "set") # we can't create tuple as a key
#}
#print(dict)
#print(type(dict)) # there is no order in dictionary
#print((dict["name"]))
#print((dict["address"]))
#print((dict["topic"]))
#dict["name"] = "nilima barick"
#dict["surname"] = "barick"
#print(dict)

# null dictionary create 
#null_dict = {}
#null_dict["name"] = "indrani"# adding value
#null_dict["DOB"] = "22.01.1997"

#print(null_dict)

# create a nested dictonary
student ={
    "name" : "wrishank maity",
    "subjects" : {
        "beng" : 87,
        "eng" : 99,
        "math" : 100,

    }

}
#print(student)
#print(student["subjects"])
#print(student["subjects"]["math"])

#print(list(student.keys())) # to see keys value of a dictionary & typecast
#print(len(student))
#print(student.values())
#print(student.items()) # we see pair of a dictionary

#print(student["name"])
#print(student.get("name")) # get is a method, 

#student.update({"city" : "delhi", "age" : 19})
#print(student)



# sets in python

#num = {1,2,3,4,5, 3, "hello", "world", "hello"}
#print(num)
#print(len(num))

collec = set() # create empty set
collec.add(1)
collec.add(3)
collec.add("nilima")
#collec.clear()
print(len(collec))

collect = {"hello", "world", "nilima", "indrani"}
print()



