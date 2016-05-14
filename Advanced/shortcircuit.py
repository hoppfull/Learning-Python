x = 1

def pr(s):
	return s

"""
if x == 0: y = pr('zero')
elif x == 1: y = pr('one')
else: y = pr('other')
print(y)
""" ## Is equivalent to:

"""
y = (x == 0 and 'zero') or (x == 1 and 'one') or ('other')
print(y)
"""## Is like:


y = lambda x: (x == 0 and 'zero') or (x == 1 and 'one') or ('other')
print(y(x))

# The point of lambda seems to be that it has to return something. Enforces purity I guess.