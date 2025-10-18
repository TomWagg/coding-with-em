Functions
=========

A function is a reusable block of code that performs a specific task. Functions help to organize code, make it more readable, and allow for code reuse.

You've already used functions like ``print()`` and ``input()``, but now it's time to create your own!

Defining a Function
-------------------

In Python, functions are defined using the ``def`` keyword, followed by the function name and parentheses containing any parameters.
Here's an example of a simple function that greets a user:

.. code-block:: python

    def greet(name):
        print("Hello, " + name + "!")

Calling a Function
------------------

When we actually want to use the function, we "call" it by using its name followed by parentheses, passing any required arguments:

.. code-block:: python

    greet("Emily")

You can also explicitly use keyword arguments when calling functions:

.. code-block:: python

    greet(name="Emily")

This can be very useful when a function has multiple parameters.


Returning values
----------------

The function we defined above doesn't return any value; it simply prints a message. However, functions can also return values using the ``return`` statement. Here's an example of a function that returns the cube of a number:

.. code-block:: python

    def cube(number):
        return number * number * number

You can call this function and store the returned value in a variable:

.. code-block:: python

    result = cube(3)
    print(result)

And you could even chain this function call to find the cube of a cube!

.. code-block:: python

    print(cube(cube(2)))


Functions with multiple (potentially optional) parameters
---------------------------------------------------------

Functions can have multiple parameters. You can also provide default values for parameters, making them optional when calling the function. Here's an example:

.. margin::

    I've sneakily introduced f-strings here! They make formatting strings much easier. The basic idea is to prefix the string with an 'f' and then you can include variables directly inside curly braces {}.

.. code-block:: python

    def introduce(name, age=-1):
        if age > 0:
            print(f"My name is {name} and I am {age} years old.")
        else:
            print(f"My name is {name}.")

    introduce("Emily", 10)
    introduce("Alice")

This function ``introduce`` has two parameters: ``name`` and ``age``. The ``age`` parameter has a default value of ``-1``, so if it's not provided when calling the function, it will use that default value. When we call ``introduce("Alice")``, it uses the default value for ``age`` and only prints the name since the age is negative.

Recursive functions
-------------------

Now these can really mess with your head, but they're super powerful! A recursive function is a function that calls itself in order to solve a problem. We know that mathematically a factorial of a number $n$ (written as $n!$) is the product of all positive integers up to $n$. For example

.. math::

    5! = 5 \times 4 \times 3 \times 2 \times 1 = 120

But we could also write a factorial function recursively, because we know that:

.. math::

    n! = n \times (n-1)!

We can define a recursive function to calculate the factorial of a number like this:

.. code-block:: python

    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    print(factorial(5))

In this example, the ``factorial`` function calls itself with a decremented value of ``n`` until it reaches the base case of ``n`` being 0 or 1. At that point, it returns 1, and the recursive calls start to resolve, ultimately calculating the factorial of the original number.

It is very important to have a base case in recursive functions to prevent infinite recursion, which can lead to a stack overflow error - a name you might have heard from the website for asking questions about programming!
