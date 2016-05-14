list = [1, 10, 16, 30]
def f(value): return value * 2
def p(value): return value > 10

result1 = []
for item in list:
	if p(item):
		result1.append(f(item))
		
# is equivalent to:
result2 = [f(item) for item in list if p(item)]


print(result1)
print(result2)