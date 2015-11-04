#Python - Assignment #11 - Selection Sort
import random

arr = []

for i in range(0,101):
	arr.append(random.randrange(0,10000))


### Selection Sort finding only MIN		
# def selectionSort(arr):
# 	counter = 0
# 	for i in range(0,len(arr)):
# 		index = i
# 		for j in range(i,len(arr)):
# 			if arr[index] > arr[j]:
# 				index = j
# 				counter += 1
# 		# temp = arr[3] = 1
# 		temp = arr[index]
# 		# arr[3] = arr[0] = 4
# 		arr[index] = arr[i]
# 		# arr[0] = temp
# 		arr[i] = temp

# 	print(counter)

# 	print(arr)


### Selection Sort find both MIN and MAX
def selectionSort(arr):
	counter = 0
	for i in range(0,len(arr)):
		minIndex = i
		maxIndex = i
		for j in range(i,len(arr)):
			if arr[minIndex] > arr[j]:
				minIndex = j
				counter += 1

		for k in range(i,len(arr)):
			if arr[maxIndex] < arr[k]:
				maxIndex = k
				counter += 1

		tempMin = arr[minIndex]
		arr[minIndex] = arr[i]
		arr[i] = tempMin

		tempMax = arr[maxIndex]
		arr[maxIndex] = arr[len(arr)-1]
		arr[len(arr)-1] = tempMax


	print(counter)

	print(arr)

selectionSort(arr)