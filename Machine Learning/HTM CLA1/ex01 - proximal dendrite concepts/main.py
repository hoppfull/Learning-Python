import numpy as np

# Random feed-forward input:
x = np.random.randint(0, 2, size=12)
print("Feed-forward input:", x)

# Random indices for feed-forward input:
y = np.random.choice(np.arange(12), size=4, replace=False)
print("Potential synapse index:", y)

# Potential synapses:
z = np.array([x[i] for i in y])
print("Potential synapse input:", z)

# Permanence values:
u = np.random.randint(10, 30, 4)
print("Permanance values:", u)

v = np.array([0 if i < 20 else 1 for i in u])
print("Permanance weights:", v)
