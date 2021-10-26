""" This is the code file for the matrix operation portion of problems set 3."""
import timeit
import numpy as np


def generate_s_matrix(n_rows: int):
    """
    Generates an NxN matrix where all edges are 1 and
    all inner values are 0 using numpy.
    """
    init_matrix = np.ones((n_rows, n_rows))
    init_matrix[1:n_rows-1, 1:n_rows-1] = 0
    return init_matrix


def generate_matrix(rows: int, cols: int):
    """Generate a rows x cols matrix with random data using numpy"""
    random_matrix = np.random.normal(size=(rows, cols))
    return random_matrix


def matrix_multiplication_loop(x_matrix:np.ndarray, y_matrix:np.ndarray):
    """Multiplies matrix x and matrix y using a nested for-loop."""
    if (x_matrix.shape[1] != y_matrix.shape[0]):
        print("Matrix dimensions don't match!")
        exit()
    else:
        result = np.zeros((x_matrix.shape[0],y_matrix.shape[1]))
        for i in range(x_matrix.shape[0]):
            for j in range(y_matrix.shape[1]):
                result[i,j]=np.dot(x_matrix[i,:],y_matrix[:,j])
        return result


# mat_100_1 = generate_matrix(100,100)
# mat_100_2 = generate_matrix(100,100)
# mat_10_1 = generate_matrix(10,10)
# mat_10_2 = generate_matrix(10,10)
def timed_multiplication_loop(x_matrix:np.ndarray, y_matrix:np.ndarray):
    """
    Times how long it takes to multiply matrix x and matrix y
    using the multiplication loop.
    100 by 100 matrix time: 1.1430001904955134e-06 seconds
    10 by 10 matrix time: 8.370006980840117e-07 seconds
    """
    result = matrix_multiplication_loop(x_matrix, y_matrix)
    time = timeit.timeit(lambda: result, number = 1)
    return result, time

def timed_multiplication_numpy(x_matrix:np.ndarray, y_matrix:np.ndarray):
    """
    Times how long it takes to multiply matrix x and matrix y
    using the numpy built-ins.
    100 by 100 matrix time: 9.520008461549878e-07 seconds
    10 by 10 matrix time: 6.919999577803537e-07 seconds
    """
    result = np.dot(x_matrix, y_matrix)
    time = timeit.timeit(lambda: result, number = 1)
    return time
