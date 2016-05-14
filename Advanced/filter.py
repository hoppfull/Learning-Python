myList = [1, 10, 11, 200]

"""
result = filter(lambda x: x > 10, myList)
for i in result: print(i)

	filter(function, list) applies function to each element in list
	and returns a filter object (not a list) with values that when
	passed to function, makes function return true.
	
	Apparently it's slow though so use list comprehension instead:
"""

def f(value): return value > 10
print([x for x in myList if f(x)])