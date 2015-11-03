#Python - Assignment #10 - Bubble Sort
import random
import datetime

arr = []

for i in range(0,101):
	arr.append(random.randrange(0,10000))

		
def bubbleSort(arr):
	temp = 0
	for i in range(0,len(arr)-1):
		for i in range(0,len(arr)-1):
			if arr[i] > arr[i+1]:
				arr[i],arr[i+1] = arr[i+1],arr[i]
	print(arr)


bubbleSort(arr)