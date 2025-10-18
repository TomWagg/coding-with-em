Randomness
==========

The ``random`` module in Python provides functions to generate random numbers and make random selections. This can be useful for simulations, games, and other applications where you need some element of chance rather than a deterministic outcome.

Let's discuss some of things you can do with the random module.

Importing the random module
---------------------------

The first thing you'll need to do is import the ``random`` module. You can do this with the following line of code:

.. code-block:: python

    import random

You can learn more about importing modules in the `imports <imports.html>`_ section.

Generating random numbers
-------------------------

The ``random`` module provides several functions to generate random numbers. Here are a few commonly used ones:

- ``random.random()``: Returns a random float between 0.0 and 1.0.
- ``random.randint(a, b)``: Returns a random integer N such that a <= N <= b.
- ``random.uniform(a, b)``: Returns a random float N such that a <= N <= b.

Here's an example of how to use these functions:

.. code-block:: python

    import random

    fraction = random.random()
    age = random.randint(1, 100)
    height = random.uniform(1.5, 2.0)

    print("Random fraction:", fraction)
    print("Random age:", age)
    print("Random height:", height)

Making random selections
------------------------

The ``random`` module also provides functions to make random selections from sequences like lists or strings. Here are a couple of useful functions:

- ``random.choice(seq)``: Returns a randomly selected element from the non-empty sequence ``seq``.
- ``random.sample(population, k)``: Returns a list of ``k`` unique elements chosen from the ``population`` sequence.

.. margin::

    What happens if you try to sample more elements than are in the list? Try it out and see!

Here's an example of how to use these functions:

.. code-block:: python

    import random

    colors = ["red", "blue", "green", "yellow"]
    random_color = random.choice(colors)
    random_colors = random.sample(colors, 2)

    print("Random color:", random_color)
    print("Random colors:", random_colors)


Shuffling a list
----------------

You can also shuffle a list randomly using the ``random.shuffle()`` function. This function modifies the list in place to rearrange its elements randomly.

.. code-block:: python

    import random

    numbers = [1, 2, 3, 4, 5]
    random.shuffle(numbers)

    print("Shuffled numbers:", numbers)

Notice that the function didn't return a new list; it changed the original list itself!


Seeding the random number generator
-----------------------------------

The random number generator in Python can be seeded to produce reproducible results. By providing a seed value using ``random.seed(a)``, you can ensure that the sequence of random numbers generated is the same each time you run your program with that seed. This can be very useful for debugging or testing.

.. code-block:: python

    import random

    random.seed(42)

    print(random.random())

This will always print the same random number every time you run the program with the seed value of 42.

Sampling based on probability
-----------------------------

Sometimes, you might want to make random choices based on specified probabilities. You might know that the probability of something occurring is 70%, how can you simulate that in your code?

You can use ``random.rand()`` to generate a random float between 0.0 and 1.0, and then check if it's less than your desired probability (e.g. 70%)! 70% of the time this will be true, and 30% of the time it will be false so it simulates the probability you want.

.. code-block:: python

    import random

    probability_of_rain = 0.7

    if random.random() < probability_of_rain:
        print("It's going to rain!")
    else:
        print("No rain today.")

This code will print "It's going to rain!" approximately 70% of the time you run it, simulating the probability of rain.

That's a brief overview of the ``random`` module in Python! There are many more functions and features available, so be sure to check out `the official documentation <https://docs.python.org/3/library/random.html>`_ for more details.


The inheritance problem uses the random module quite a bit, so that could be a great place to test your knowledge! You can find that problem `here <../problems/inheritance.html>`_.