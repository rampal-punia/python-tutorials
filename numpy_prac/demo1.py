import numpy as np


def create_array(x):
    np.array(float(x))


def get_array():
    return np.empty((), dtype=np.float).tolist()


print(create_array(123.456))
print(get_array())
