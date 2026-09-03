#What’s the difference between a list and a tuple?
""" The main difference between list and Tuple is mutability
List: List is mutable means we can add,remove,update and change items in list
list is defined in []
list = ["apple",8,"class"]
Tuple: Tuple is immutable means we cannot add,remove,update and change items once created
tuple is defined in ()
items = ("chair",9,"pen")"""

#Write a function that returns the square of a number.
def sq(number):
    return number*number

print(sq(7))

#What does *args do in a function signature?
# *args in function are used to pass multtiple values as arguments
def add(*args):
    return sum(args)

print(add(5,7,4))

#What’s the output of a basic for loop over range(5)?
for i in range (5):
    print(i)
#the output will be 0 to 4 because it starts from 0 and didn't include 5 


#What is a dictionary comprehension?
#it is used to to create key and values in one line using loop
sq = {x: x**2 for x in range(1, 6)}
print(sq)

#Build a small command-line program: takes a list of numbers as input, returns mean, median, mode, min, max 
a = []
n = int(input("Number of elements you want to enter: "))
for i in range(n):
    b = int(input("Enter a number: "))
    a.append(b)
print(a)
print("Larger number in list is ",max(a))
print("Smaller number in list is ",min(a))
print("Sum of list is: ",sum(a))
print("Length of list is: ",len(a))
print("mean of list is: ",sum(a)/len(a))
#median 
a.sort()
if len(a) % 2 == 0:
    median = (a[len(a)//2 - 1] + a[len(a)//2]) / 2
else:
    median = a[len(a)//2]
print("the median of all numbers is:", median)


