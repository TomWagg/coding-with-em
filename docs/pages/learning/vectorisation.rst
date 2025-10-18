Vectorisation
=============

Vectorisation is the process of converting an algorithm from operating on a single value at a time to operating on a set of values at once. This is often done to improve performance, as modern processors are designed to handle multiple data points simultaneously.

We're going to explore vectorisation using the popular NumPy library, which provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.

Installing NumPy
----------------

If you haven't already installed NumPy, you can do so using pip. Open your terminal or command prompt and run the following command:

.. code-block:: bash

    pip install numpy


Creating NumPy Arrays
---------------------

To get started with vectorisation, we first need to create numpy arrays. Here's how you can create a simple NumPy array:

.. code-block:: python

    import numpy as np

    array = np.array([1, 2, 3, 4, 5])
    print("NumPy Array:", array)
 

Vectorised Operations
---------------------

One of the main advantages of using NumPy is the ability to perform vectorised operations. This means you can apply operations to entire arrays without the need for explicit loops. Here's an example of adding two arrays together:

.. code-block:: python

    import numpy as np

    array1 = np.array([1, 2, 3])
    array2 = np.array([4, 5, 6])

    result = array1 + array2
    print("Result of Addition:", result)


Vectorised Functions
--------------------

NumPy also provides a variety of vectorised functions that can be applied to arrays. For example, you can compute the sine of each element in an array:

.. code-block:: python

    import numpy as np

    angles = np.array([0, np.pi/2, np.pi])
    sine_values = np.sin(angles)
    print("Sine Values:", sine_values)

Broadcasting
------------

Broadcasting is a powerful mechanism in NumPy that allows operations to be performed on arrays of different shapes. For example, you can add a scalar value to an array:

.. code-block:: python

    import numpy as np

    array = np.array([1, 2, 3])
    scalar = 5

    result = array + scalar
    print("Result of Adding Scalar:", result)

Useful numpy functions
----------------------

NumPy provides many useful functions for working with arrays. Here are a few examples:

.. code-block:: python

    import numpy as np

    array = np.array([1, 2, 3, 4, 5])

    mean = np.mean(array)
    std_dev = np.std(array)
    sum_array = np.sum(array)

    print("Mean:", mean)
    print("Standard Deviation:", std_dev)
    print("Sum:", sum_array)


You can also create ranges of numbers easily using numpy, or linear spaced numbers:

.. code-block:: python

    import numpy as np

    range_array = np.arange(0, 10, 2)  # From 0 to 10 with step of 2
    linspace_array = np.linspace(0, 1, 5)  # 5 numbers from 0 to 1

    print("Range Array:", range_array)
    print("Linspace Array:", linspace_array)


Time benefits of vectorisation
------------------------------

So why is vectorisation so great? The main benefit is speed. By leveraging optimized C and Fortran libraries under the hood, NumPy can perform operations on large datasets much faster than traditional Python loops.

Here's a simple comparison of vectorised vs non-vectorised code for adding two large arrays:

.. code-block:: python

    import numpy as np
    import time

    size = 1e7
    array1 = np.random.rand(size)
    array2 = np.random.rand(size)

    # Non-vectorised approach
    start_time = time.time()
    result_non_vectorised = []
    for i in range(size):
        result_non_vectorised.append(array1[i] + array2[i])
    end_time = time.time()
    print("Non-vectorised Time:", end_time - start_time)

    # Vectorised approach
    start_time = time.time()
    result_vectorised = array1 + array2
    end_time = time.time()
    print("Vectorised Time:", end_time - start_time)

On my laptop, the non-vectorised approach takes about 1.5 seconds to complete, while the vectorised approach takes only about 0.008 seconds!

These are just a few examples of how vectorisation with NumPy can simplify your code and improve performance. As you continue to explore NumPy, you'll find many more functions and techniques to help you work with data efficiently! Check out `the official NumPy documentation <https://numpy.org/doc/stable/>`_ for more information.