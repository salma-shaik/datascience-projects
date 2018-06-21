import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced
    # predictions.
    #
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE

    num_diff = data - predictions
    num_diff_sqr = np.square(num_diff)
    # print(num_diff_sqr.sum())
    num = np.sum(num_diff_sqr)

    ave_data = np.mean(data)

    den_diff = data - ave_data
    den_diff_sqr = np.square(den_diff)
    den = np.sum(den_diff_sqr)

    r_squared = 1 - (num/den)
    return r_squared


data = np.array([2,5,8,3])
predictions = np.array([3,9,1,6])

print(compute_r_squared(data, predictions))
