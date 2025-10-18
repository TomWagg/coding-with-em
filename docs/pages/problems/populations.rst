populations
===========

In this problem, you'll simulate the growth of a rabbit population over time using loops and conditions.

.. figure:: ../../_static/rabbits.png
    :align: center
    :width: 300px
    
    Rabbits, rabbits everywhere!

Overview
--------

Picture a remote island, filled with luscious green grass and lettuce and perfect weather. A few rabbits arrive on the island and decide to make it their new home. As you know, there's nothing a rabbit loves more than to multiply! Your task is to write a program that simulates the growth of the rabbit population on this island over a number of months.

You will add code to the ``scripts/populations.py`` file to model the rabbit population growth.

You can run this program from the command line, passing in parameters for the initial population size, fertility rate, and number of months to simulate. For example:

.. code-block:: bash

    python scripts/populations.py -s 10 -f 4 -m 3

I've set up the command line argument parsing for you; your job is to implement the population growth logic. Right now it'll always just return 0 (oh no, where did the rabbits go?!).

Part one
--------

Start by simulating the rabbit population growth without any constraints. You'll be modifying the ``growth`` function in ``scripts/populations.py``. The function takes three parameters:

- ``n_start``: The initial number of rabbits on the island
- ``fertility``: The average number of offspring each *pair* of rabbits produce per month
- ``months``: The number of months to simulate

These are very romantic rabbits that mate for life! That means that only pairs of rabbits can produce offspring. For example, if there are 10 rabbits on the island, there are 5 pairs, and if the fertility rate is 4, then those 5 pairs will produce a total of 20 new rabbits in one month. But if there were 11 rabbits, there would still only be 5 pairs (the extra rabbit is single 😭), and they would still only produce 20 new rabbits in one month.

Your task is to implement the population growth logic in the ``growth`` function. The function should return the total rabbit population after the specified number of months.

Here are some test cases your function should pass:

.. code-block:: python

    # expected output: 3
    python scripts/populations.py -s 2 -f 1 -m 1

    # expected output: 1234
    python scripts/populations.py -s 10 -f 1 -m 12

    # expected output: 67108865
    python scripts/populations.py -s 5 -f 2 -m 24

    # expected output: 21767823360
    python scripts/populations.py -s 10 -f 10 -m 12


