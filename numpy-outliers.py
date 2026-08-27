#Broadcasting
"""broadcasting in numpy is a mechanism that allows to perform operations on arrays of different shapes"""
import numpy as np
arr1 = np.array([10,20,45])
arr2 = [1]
arr3 = arr1 + arr2
print(arr3)

#Difference between .reshape() and .flatten()?
"""reshape:
#Reshape is the function that is used reshape array """
arr = np.array([10,20,45,56])
print(arr.reshape(2,2))
#Flatten:
"""Flatten is used to change the dimension of the array"""

#What does axis=0 vs axis=1 mean in np.sum()?
"""axis=0 is usd to perform sum operation in rows
#axis=1 is usd to perform sum operation in columns"""



#How do you generate a random array of shape (5,5)?
arr = np.random.rand(5,5)
print(arr)



#How do you select all rows where a column value > 10 in a 2D array?
"""by giving condition in "where" function and axis=0"""