# Implement bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j +1]:
                arr[j], arr[j +1] = arr[j + 1], arr[j]
                return arr

arr = [ 34,56,28,34,10,15]
print("Original array: ", arr)
print("Sorted array: ", bubble_sort(arr))


# Implement selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
            arr[i], arr[min_index] = arr[min_index] , arr[i]
print("sorted array: ", selection_sort)


# Inplement insertion sort

arr = [9, 7, 8,3,1]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        j -= 1
    arr[j + 1] = key 
print("sorted array: ", arr)


# Demonstrate stable and unstable array
students = [
    ("puja", 80),
    ("diya", 60),
    ("maya", 90),
    ("gita", 70)
]
sorted_students = sorted(students, key=lambda x: x[1])
print("stable sort: ")
for student in sorted_students:
    print(student)
