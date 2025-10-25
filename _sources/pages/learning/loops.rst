Loops
=====

Often when programming, we want to repeat a set of instructions multiple times. For example, we might want to print out the numbers from 1 to 10, or process each item in a list. This is where loops come in handy. Loops allow us to execute a block of code multiple times, either for a specific number of iterations or while a certain condition is true.

For Loops (Definite Iteration)
------------------------------

Basic syntax
^^^^^^^^^^^^

A ``for`` loop is used to loop a specific number of times, often iterating over a sequence like a list or a range of numbers. These loops are great when you know in advance how many times you want to repeat the code. The syntax comes in two parts: the loop header and the loop body. It looks like this:

.. code-block:: python

    for item in sequence:
        # Loop body: code to be repeated

Fixed number of loops
^^^^^^^^^^^^^^^^^^^^^

A very common use of ``for`` loops is to iterate over a range of numbers using the ``range()`` function. For example, to print the numbers from 1 to 5, you can use the following code:

.. margin::

    Note: The ``range()`` function generates numbers starting from the first argument up to, but not including, the second argument. Such that ``range(1, 6)`` produces the numbers 1, 2, 3, 4, and 5.

    This may seem weird at first, but it's useful for list indices that are zero-based (starting from 0).

.. code-block:: python

    for i in range(1, 6):
        print(i)

In addition to printing out values, we can use ``for`` loops to perform calculations. For example, let's calculate the sum of the first 10 natural numbers:

.. code-block:: python

    total = 0
    for i in range(1, 11):
        total = total + 1
    print("The sum of the first 10 natural numbers is:", total)

In this example, we initialize a variable ``total`` to 0, then use a ``for`` loop to add each number from 1 to 10 to ``total``. Finally, we print the result.

Looping through a sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also use ``for`` loops to iterate over the items in a list. For example, let's say we have a list of fruits and we want to print each fruit:

.. code-block:: python

    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)

Or if we have two different lists and we want to print out the first three items in each list, we can use a ``range`` loop with indexing:

.. code-block:: python

    colors = ["red", "green", "blue"]
    animals = ["cat", "dog", "rabbit", "elephant", "giraffe"]
    for i in range(3):
        print("Imagine a", colors[i], animals[i])

Importantly, we only loops 3 times here, even though the ``animals`` list has 5 items. This is because we specified the range to be 3. If we tried to loop 5 times, we would get an error when trying to access ``colors[3]`` and ``colors[4]``, since the ``colors`` list only has 3 items (indices 0, 1, and 2).

.. admonition:: Exercise

    Try modifying that last example to loop 5 times and see what error you get! Then add two more colors to the ``colors`` list to fix the error.

Even more things are iterable in Python, including strings! Here's an example of looping through each character in a string:

.. code-block:: python

    message = "Hello"
    for char in message:
        print(char)


While Loops (Indefinite Iteration)
----------------------------------

Basic syntax
^^^^^^^^^^^^

A ``while`` loop is used to repeat a block of code as long as a certain condition is true. These loops are useful when you don't know in advance how many times you need to repeat the code. The syntax also comes in two parts: the loop header and the loop body. It looks like this:

.. code-block:: python

    while condition:
        # Loop body: code to be repeated

Here, ``condition`` is an expression that evaluates to either ``True`` or ``False``. As long as the condition is ``True``, the indented block of code under the ``while`` statement will be executed repeatedly. Once the condition becomes ``False``, the loop will stop.

The ``condition`` can use any comparison operators or logical operators you've learned about in the conditions lesson!

Example: Counting down
^^^^^^^^^^^^^^^^^^^^^^

You can use a ``while`` loop to do the same counting task we did with a ``for`` loop, but this time counting down from 5 to 1:

.. code-block:: python

    count = 5
    while count > 0:
        print(count)
        count = count - 1
    print("Liftoff!")

In this example, we start with a variable ``count`` set to 5. The ``while`` loop continues as long as ``count`` is greater than 0. Inside the loop, we print the current value of ``count`` and then decrease it by 1. When ``count`` reaches 0, the condition becomes ``False``, and the loop ends, printing "Liftoff!".

.. admonition:: Warning

    Be careful with ``while`` loops! If the condition never becomes ``False``, the loop will run forever, causing your program to hang. This is called an "infinite loop." Always make sure that something inside the loop will eventually change the condition to ``False``.

    If you accidentally create an infinite loop while testing your code, you can usually stop it by pressing ``Ctrl + C`` in your terminal or command prompt.

    .. figure:: ../../_static/sisyphus.jpeg
        :align: center
        :width: 500px

        Don't be like Sisyphus, stuck in an endless loop!


Example: Guessing game
^^^^^^^^^^^^^^^^^^^^^^

Here's an example of a simple guessing game using a ``while`` loop:

.. code-block:: python

    secret_number = 7
    guess = -1

    while guess != secret_number:
        guess = int(input("Guess the secret number (between 1 and 10): "))
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the secret number.")

In this example, the program keeps asking the user to guess the secret number until they get it right. The loop continues as long as the user's guess is not equal to the secret number. Inside the loop, we provide feedback on whether the guess was too low or too high.

Problem time!
-------------

Now that you've learned about loops and conditions, try applying this knowledge in the `populations <../problems/populations.html>`_ problem in the Problems section.