import numpy as np
print(np.array([1,2,3,4,5,6]))

#output zeros
print(np.zeros(4))

#2D Array consisting of ones
print(np.ones([4,5]))

print(np.full([2,6], 9))

x = np.full([10, 20], 7, dtype = int)
print(x)
print(str(x.size) + " items in the matrix (size)")
print(str(x.dtype) + " datatype of elements contained inthe matrix")
print(str(x.shape) + " the shape of the matrix")
print(str(x.ndim) + "D. Number of dimensions of the matrix")

##np.reshape(arg, [r, c]) setting cols to -1 automatically decides the number of cols
print("This is a reshaped matrix : \n", np.reshape(x, [4, -1]))

#Insert or modify an element
print()
print("The element at row 3, column 5 is modified \n")
x[3, 5] = 33
print(x)
print()
print("The element at row 7 column 9 is modified \n")
x[7, 9] = 23.9421
print(x)
print()

#generating random integers
print("Generating random numbers, given a certain size of elements")
x = np.random.randint(20, size = 6)
print(x)

print(x[:2])
print(x[-1])
print(x[0::2])
print("-" * 30)

#Generating a 2D array for randomized integers
print("Generating 2D Array for randomized integers \n")
x = np.random.randint(5, size = [3,4])
print(x)
print(" ")
print("row at index 2 : ", x[2])
print()

#concatenating/joining 2 arrays
x = np.array([1,4,6,8,0])
y = np.array([3,2,1,7,5])
print("concatenate array a and b : ", np.concatenate([x,y]))
print("-" * 30)

#vstack and hstack for multidimensional array
x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7], [6, 5, 4]])
print(np.vstack([x, grid]))
print("-" * 30)

#Simple Functions on Numpy
print("np.arange function")
""" Provides a range of numbers from start to end """ 
x = np.arange(1, 10 + 1)
print("Range of x(1, 11): ", x)
print("The square of x : ", x ** 2)
print(x // 4)
print()

x = [-2, -1, 1, 2]
print("Absolute Value : ", " \t ", np.abs(x))
print("Exponential : ", " \t  ", np.exp(x))
print("Standard Deviation : ", "\t ", np.std(x))
print("Index of smallest element : ", np.argmin(x))
print("Index of largest element :  ", np.argmax(x))
#print("Percentile : ", np.percentile(x))
print(help(np.exp))

x = [4,9,7,2.5]
print("Logarithm : ", np.log(x))
print("-" * 30)

#Boolean operations
x = np.random.randint(4, 5)
print("random int of 0 - 4 : ", x)
print("Boolean Expression (x > 7) : ", x > 7)
print(np.where(x == 4)) # return values with certain properties
print("-" * 30)

#Agregation
x = np.random.randint(100, size = 50)
print((x))
print(np.sum(x))
print("-" * 30)
#Broadcasting
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
print(a + b)
print(a + 7)
M = np.ones((3, 3))
print("M is: \n", M)
print("M+a is: \n", M+a)


