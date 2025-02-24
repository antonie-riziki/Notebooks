import numpy as np
print(np.version)

x = np.arange(10)
print(x)

x = np.full([3,3], True, dtype = bool)
print(x)

arr = np.array([1,2,3,4,5,6,7,8,9,10])
arr[arr % 2 == 1] = -1
print(arr)

x = np.arange(10)
y = np.where(x%2==1)
print(x)
print(y)

a = np.arange(10)
print(a)
a = np.reshape(a, [2, 5])
print(a)

a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
print(a)
print(b)
print(np.vstack([a, b]))
print(np.hstack([a, b]))

a = np.array([1,2,3])
print(np.r_[np.repeat(a, 3), np.tile(a, 3)])

x = np.array([1,2,3,2,3,4,3,4,5,6])
y = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.intersect1d(x, y))

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.setdiff1d(a, b))

x = np.array([1,2,3,2,3,4,3,4,5,6])
y = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.where(x != y))

x = np.array([1,2,35,2,3,4,13,4,5,61])
y = np.where(x > 5)
#alternatively
print(x[(x >= 5)])
print(x[y])
#print(np.Infinity(x))
print(np.isfinite(x))
print(np.isnan(x))

