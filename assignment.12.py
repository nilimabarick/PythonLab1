# Use lambda function to find square of a number

lam_fun = lambda x : x * x
print(lam_fun(8))

# use map and filter together in a program
numbers = [ 2, 3, 4, 5, 6,7]
def is_even(n):
    return n % 2 == 0
def square(n):
    return n * n

even_numbers = list(filter(is_even, numbers))
square_evens = list(map(square, even_numbers))

print(even_numbers)
print(square_evens)

# use reduce to calculate product of element
from functools import reduce
num = [2,3,4,5]
product = reduce(lambda x, y: x * y, num)
print(product)


#perform array operation using Numpy



import numpy as np

A = np.array([22, 24, 38, 34])
B =np.array([11, 12, 6, 2])

# Arithmetic operation

print("Addition: ", A + B )
print()

print("Subtraction: ", A - B )
print()

print("Multiplication: ", A * B )

print()
print("Division: ", A / B )

# logical operation


print(" Equal: ", A == B)
print(" Not Equal: ", A != B)
print("geater: ", A > B)
print(" Less: ", A < B)

data = np.array([10, 20, 30, 40, 50, 60])

print("Maximun: ", np.max(data))
print("Minimum: ", np.min(data))
print("Sum: ", np.sum(data))
print("Mean: ", np.mean(data))
print("Median: ", np.median(data))
print("Standard Deviation: ", np.std(data))

# Data Analysis Using Pandas DataFream

import pandas as pd

data = {
    "Name": ["Priyanka", "Puja", "Rakesh", "Jeevita"],
    "Age": [20,23,21,24,],
    "Marks": [89,82,93,96]
}
df = pd.DataFrame(data)
print(df)

print()
print("Columns: ", df.columns)

print("First Row: ", df.head())
print()
print("Mean: ", df["Marks"].mean())
print("Median: ", df["Marks"].median())
print("Mean: ", df["Marks"].mode())
print("Standard Deviation: ", df["Marks"].std())

# Condition Data by Marks 
print("Students with Marks > 85: ")
print(df[df["Marks"] > 85])


# Sort data by marks
print("\nSorted Data: ")
sorted_df = df.sort_values(by="Marks", ascending = False)
print(sorted_df)


