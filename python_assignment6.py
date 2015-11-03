#Python - Assignment #6 - Scores and Grades

def grades(score):
	if score >= 90:
		return "Score: %s; Your grade is A" % score
	elif score >= 80 and score < 90:
		return "Score: %s; Your grade is B" % score
	elif score >= 70 and score < 80:
		return "Score: %s; Your grade is C" % score
	elif score >= 60 and score < 70:
		return "Score: %s; Your grade is D" % score
	else:
		return "You'll need to try way harder"

print "Scores and Grades"

index = 0

while index < 10:
	score = input()
	print grades(score)
	index += 1
print "End of the program.  Bye!"


