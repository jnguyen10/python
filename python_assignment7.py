#Python - Assignment #7 - Coin Flip

import random

index = 1
even_count = 0
odd_count = 0
while index <= 5000:
	random_num = random.random()
	if round(random_num) == 1:
		even_count += 1
		print "Attempt #%s: Throwing a coin... It's a head!  Got" % index, even_count,"head(s) so far and", odd_count, "tail(s) so far."
	else:
		odd_count += 1
		print "Attempt #%s: Throwing a coin... It's a tail!  Got" % index, even_count,"head(s) so far and", odd_count, "tail(s) so far."
	index += 1
