#Python - Assignment #9 - Stars


# Part I
x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars_partI(arr):
	for i in arr:
		print i*"*"

draw_stars_partI(x)

# Part II
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars_partII(arr):
	for i in arr:
		if isinstance(i, basestring):
			letter = i[0].lower();
			print len(i)*letter
		else:
			print i*"*"

draw_stars_partII(y)

