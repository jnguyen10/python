import re

# julia = ('julia','roberts', 1967, 'pretty woman', 'actress')

# # (first_name, last_name, birth_year, movie, title) = julia

# # # print first_name
# # # print last_name
# # # print birth_year

# # for index, item in enumerate(julia):
# # 	print(str(index)+" = "+str(item))

# num = (1, 5, 3, 7, 9, 12)
# newNum = sorted(num)
# print newNum


# print tuple(reversed(num))


def get_square(s):
	p = 4 * s
	a = s * s
	return (p, a)

result = get_square(5)

print result

# weekend = {"Sun": "Sunday", "Sat": "Saturday"}
# weekday = {"Mon": "Monday", "Tues": "Tuesday"}

# print cmp(weekend,weekday)

# for data in weekend:
# 	print data

# for key in weekend.iterkeys():
# 	print key

# for val in weekend.itervalues():
# 	print val

# for key, data in weekend.items():
# 	print key, " - ", data

# weekend.update(weekday)

# print weekend

# context = {
# 	'questions': [
# 	{ 'id': 1, 'content': 'Why is there a light?'},
# 	{ 'id': 2, 'content': 'Why don\'t you try it?'}
# 	]
# }

# for key, data in context.items():
# 	for value in data:
# 		print "Question #", value["id"], ":", value["content"]
# 		print "----"

# dish = ["pizza","hamburger","pasta"]
# country = ["italia", "america"]

# # foods = zip(dish, country)

# # print foods

# # foods_dict = dict(foods)

# # print foods_dict


# country.append("italy")

# print country

# for val in "string":
# 	if val == "i":
# 		continue
# 	print(val)

# match = re.search(r'i?', 'abcdef21314')
# if match:
# 	print 'found', match.group()
# else:
# 	print 'not found'

str = 'blue b-real@google.com and here\'s another email address a@google.com'

# emails = re.findall(r'[\w.-]+@[\w\.-]+',str)

# for emails in emails:
# 	print emails

print re.sub(r'([\w.-]+)@([\w.-]+)', r'\1@yo-yo-dyne.com', str)




raw_input("\n\nPress the enter key to exit.")