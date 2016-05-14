import time

# Set start time:
t0 = time.perf_counter()

for i in range(100000):
	5 + 5

# Set stop time:
t1 = time.perf_counter()

# Round delta time in millisec to three decimals and print:
print(round((t1-t0)*1000, 3))