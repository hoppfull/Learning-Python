myList = [1, 10, 11, 200]

"""
result = map(lambda x: x*2, myList)
for i in result: print(i)

	map(function, list) applies function to each element in list
	and returns a map object (not a list).
	
	Apparently it's slow though so use list comprehension instead:
"""

def f(value): return value * 2
print([f(x) for x in myList])