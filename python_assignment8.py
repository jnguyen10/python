#Python - Assignment #8 - Names

users = {
	'Students': [
		{'first_name': 'Michael', 'last_name': 'Jordan'},
		{'first_name': 'John', 'last_name': 'Rosales'},
		{'first_name': 'Mark', 'last_name': 'Guillen'},
		{'first_name': 'KB', 'last_name': 'Tonel'}
	],
	'Instructors': [
		{'first_name': 'Michael', 'last_name': 'Choi'},
		{'first_name': 'Martin', 'last_name': 'Rosales'}
	]
}

for key, data in users.items():
	index = 1
	if len(data) > 2:
		print "Students"
	else:
		print "Instructors"
	for value in data:
		nameSum = len(value["first_name"])+len(value["last_name"])
		print index, "-", value["first_name"].upper(), value["last_name"].upper(), "-", nameSum
		index += 1
