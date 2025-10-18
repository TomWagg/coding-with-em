Visualisation
=============

There are many ways to visualise data in Python. We're going to focus on the use of the popular Matplotlib library, which provides a wide range of tools for creating static, animated, and interactive visualisations in Python.

Installing Matplotlib
---------------------

If you haven't already installed Matplotlib, you can do so using pip. Open your terminal or command prompt and run the following command:

.. code-block:: bash

    pip install matplotlib

Creating a simple line plot
---------------------------

To create a simple line plot, you can use the following code:

.. code-block:: python

    import matplotlib.pyplot as plt

    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    # Create a line plot
    plt.plot(x, y)

    # Add labels and title
    plt.xlabel('X-axis Label')

    plt.show()

