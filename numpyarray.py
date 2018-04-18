# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a Numpy array from baseball: np_baseball
np_baseball = np.array(baseball) * 2

# Print out type of np_baseball
print(type(np_baseball))
print(np_baseball)
light = np_baseball < 220
print(np_baseball[light])
print(np.array([True, 1, 2]) + np.array([3, 4, False]))
x = [1, 2, 3, 4, 5]
x[1]

np_x = np.array(x)
print(np_x[np_x > 2])