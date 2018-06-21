import numpy as np

# array1 = np.array(([1, 2], [3, 4]), float)
# array2 = np.array(([5, 6], [7, 8]), float)
#
# print(array1 * array2)
# print(np.dot(array1, array2))

# array1 = np.array(([1, 2], [3, 4]), float)
# array2 = np.array([5, 6], float)

array1 = np.array([[1, 2]], float)
array2 = np.array(([2, 4, 6], [3, 5, 7]), float)

# print("Mult: ",array1 * array2)
print("Mult: ",np.multiply(np.matrix(array1) * np.matrix(array2)))
print("Dot:", np.dot(array1, array2))

print()

# array3 = np.array(([1, 2], [3, 4]), float)
# array4 = np.array(([5], [6]), float)
#
# print("Mult: ",array3 * array4)
# print("Dot:", np.dot(array3, array4))