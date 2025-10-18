greeting
========

Welcome to your first coding problem! We're going to apply what you've learned about variables to create a simple greeting program.

Part one
--------

.. margin::

    Hint: use the ``input()`` function to get user input.

Create a program (in ``scripts/greeting.py``) that asks the user for their name and then greets them with a personalized message. For example, if the user inputs "Alice", the program should output "Hello, Alice! Welcome to the coding world!"

.. code-block:: bash
    
    python scripts/greeting.py
    "Please enter your name: Tom"
    "Hello, Tom! Welcome to the coding world!"

Part two
--------

.. margin::

    Hints
    - Remember to convert the age from a string to an integer before performing calculations.
    - You can calculate the number of seconds in a year by series of multiplications

Modify your program to also ask for the user's age. After greeting them, the program should tell them how many seconds they have lived so far (don't worry about leap years or exact dates; just use 365 days per year). For example, if the user inputs "Joe" and "26", the program should output "Hello Joe! You have lived for at least 819936000 seconds!"

.. code-block:: bash
    
    python scripts/greeting.py
    "Please enter your name: Joe"
    "Please enter your age: 26"
    "Hello Joe! You have lived for at least 819936000 seconds!"