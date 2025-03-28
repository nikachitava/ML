import numpy as np




# m = np.array([6, 2, 18, 5, 6, 23])
#
#
# min_val = np.min(m)
# max_val = np.max(m)
# min_max_slaced = (m - min_val) / (max_val - min_val)


# task 2
# arr = np.array([[1, 67, 9], [2, 67, 4], [4, 5, 6]])
# uniq = np.unique(arr)
# print("unique: ", uniq)

import numpy as np


def generate_spiral_matrix(N):
    # Create an empty N x N matrix
    matrix = np.zeros((N, N), dtype=int)

    # Define the four directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    current_value = 1  # Start filling with 1
    x, y = 0, 0  # Starting position at the top-left corner
    dir_idx = 0  # Start by moving right

    while current_value <= N * N:
        # Fill the current position with the current value
        matrix[x, y] = current_value
        current_value += 1

        # Calculate the next position
        next_x = x + directions[dir_idx][0]
        next_y = y + directions[dir_idx][1]

        # Check if the next position is within bounds and not already filled
        if (0 <= next_x < N) and (0 <= next_y < N) and matrix[next_x, next_y] == 0:
            x, y = next_x, next_y
        else:
            # Change direction (right -> down -> left -> up -> right -> ...)
            dir_idx = (dir_idx + 1) % 4
            x += directions[dir_idx][0]
            y += directions[dir_idx][1]

    return matrix


# Example usage:
N = 5  # Size of the matrix
spiral_matrix = generate_spiral_matrix(N)
print(spiral_matrix)






