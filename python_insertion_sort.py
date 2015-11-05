#Python - Assignment #12 - Insertion Sort
import random

newuserList = []

for i in range(0,101):
	newuserList.append(random.randrange(0,10000))


def insertionSort(userList):
	for i in range(0,len(userList)):
		index = i
		tempValue = userList[i]
		counter = 0
		for j in range(i,-1,-1):
			# print "tempValue:", tempValue
			# print "userList[i]:", userList[i]
			# print 'userList[j]:', userList[j]
			# print 'i', i
			# print 'j', j
			if tempValue < userList[j]:
				# print "tempValue:", tempValue
				# print "userList[index]:", userList[index]
				# print "userList[i]", userList[i]
				# print 'userList[j]:', userList[j]
				# print "i",i , "j",j, "index", index
				# print "shift: ", userList[j], userList[index]
				# print "current userList:", userList
				userList[index] = userList[j]
				
				index = j
				counter += 1
				# print "tempValue:", tempValue
				# print "userList[index]:", userList[index]
				# print "userList[i]:", userList[i]
				# print "userList[j]:", userList[j]
				# print "i", i, "j", j, "index", index
				# print "shift: ", userList[j], userList[index]
				# print "updated userList", userList

		userList[index] = tempValue
	
	print(counter)
		
	print(userList)


insertionSort(newuserList)