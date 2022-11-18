# Numpy

A fundamental scientific computing Python library that provides a multidimensional array object, and lots of functionalities for fast operations on these arrays.

[Numpy Quick Start](https://numpy.org/doc/stable/user/quickstart.html)

## Basics
NumPy’s main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type. 

In NumPy dimensions are called axes.

For example:
```python
[2,3,4]     # 1D Array   

[[2,3,4],   # 2D Array
[3, 4, 5], 
[4 ,5 ,6]]

[[[1., 1., 1., 1.],     # 3D Array
    [1., 1., 1., 1.],
    [1., 1., 1., 1.]],

    [[1., 1., 1., 1.],
    [1., 1., 1., 1.],
    [1., 1., 1., 1.]]]
```

```python
import numpy as np
a = np.arange(15).reshape(3, 5)

print(a)

# Output:
# array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14]])

# Get shape of the ndarray
print(a.shape)
# Output:
(3, 5)

# Get shape of the ndarray

