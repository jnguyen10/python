#Python - Assignment #5 - Multiply

def multiply(arr, i):
	index = 0
	newArr = []
	while index < len(arr):
		newArr.append(arr[index]*5)
		index += 1
	return newArr

a = [2,4,10,16]
b = multiply(a, 5)
print(b)