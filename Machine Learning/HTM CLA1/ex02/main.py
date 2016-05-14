import numpy as np

x = np.random.randint(1, 2, size=(10, 10))
# print(x)

y = np.array([np.arange(8) + 1 for _ in range(8)])
z = np.fliplr(y) * y * np.rot90(np.fliplr(y) * y)
print(z)
