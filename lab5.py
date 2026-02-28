
# lab problem: online shopping cart analysis
# you are buliding a simple system to analyze customar purcheses in an online store
# each customer buys multiple items
# problem statement
# take input of purchesed item separeted by space
# store them in a list
# convert item into a set to find unique product purchesd
# store information in a tuple
# store name
# location
# GST number
# perform follwing
# print total item purches
# print unique item purches
# print how many time each item was bought
# try to modifying the tuple and observe what hanned

item_input = input("enter purches item separated by space : ").lower()
item_list = item_input.split(" ")
unique_item = set(item_list)
store_info = ('SuperMart', 'Ranihati', 'GST6485')
total_item = len(item_list)
#for item in item_list:
    #total_item +=1
unique_total_items = 0
for item in unique_item:
    unique_total_items += 1

print("\n--- shopping summery---")
print("total item purchesd : ", total_item)
print("total unique item purchesd : ", unique_total_items)
print("item purchesd count: \n")
for item in unique_item:
    print(item, ":", item_list.count(item))

try:
    store_info[0] = "SmartBazar"
except TypeError:
    print("\n Tuple modification error")

print("store info", store_info)


