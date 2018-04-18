baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(np_baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat = np_mat * 2
print(np_mat)
np_mat = np_mat + np.array([10, 10])
np_mat = np_mat + np_mat
print(np_mat)