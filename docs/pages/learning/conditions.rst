Conditions
==========

In programming, conditions are used to make decisions in your code. They allow you to execute certain blocks of code only if specific criteria are met. This is typically done using ``if``, ``elif``, and ``else`` statements, though once we talk about loops, we will also see how conditions can be used in conjunction with them.

.. raw:: html

    <img src="../../_static/fork.jpg" style="display: block; margin-left: auto; margin-right: auto; width: min(100%, 500px);"/>

If Statement Syntax
-------------------

The basic syntax of an ``if`` statement in Python looks like this:

.. code-block:: python

    if condition:
        # Code to execute if the condition is true
        print("Only runs if condition is true")

Here, ``conditions`` is an expression that evaluates to either ``True`` or ``False``. If the condition is ``True``, the indented block of code under the ``if`` statement will be executed. You can see here that **indentation is very important** in Python, as it defines the "scope" of the code blocks.

.. epigraph::

    In Python, indentation is not just for readability; it is a fundamental part of the syntax that defines the scope of different blocks. Make sure to use consistent indentation (usually 4 spaces) throughout your code to avoid errors.

This can be followed by optional ``elif`` (else if) and ``else`` statements to handle multiple conditions:

.. code-block:: python

    if condition1:
        # Code to execute if condition1 is true
        print("Condition 1 is true")
    elif condition2:
        # Code to execute if condition2 is true (when condition1 is false)
        print("Condition 2 is true")
    else:
        # Code to execute if neither condition1 nor condition2 is true
        print("Neither condition is true")

Operators for Conditions
------------------------

Comparison Operators
^^^^^^^^^^^^^^^^^^^^

To create conditions, we often use comparison operators to compare values. Here are some common comparison operators in Python:

.. list-table:: Comparison operators
    :header-rows: 1

    * - Operator
      - Description
      - Example
      - Example explanation
    * - ``==``
      - Equal to
      - ``x == 5``
      - Checks if ``x`` is equal to ``5``
    * - ``!=``
      - Not equal to
      - ``x != 5``
      - Checks if ``x`` is not equal to ``5``
    * - ``<``
      - Less than
      - ``x < 5``
      - Checks if ``x`` is less than ``5``
    * - ``>``
      - Greater than
      - ``x > 5``
      - Checks if ``x`` is greater than ``5``
    * - ``<=``
      - Less than or equal to
      - ``x <= 5``
      - Checks if ``x`` is less than or equal to ``5``
    * - ``>=``
      - Greater than or equal to
      - ``x >= 5``
      - Checks if ``x`` is greater than or equal to ``5``

Logical Operators
^^^^^^^^^^^^^^^^^

.. list-table:: Logical operators
    :header-rows: 1

    * - Operator
      - Description
      - Example
      - Example explanation
    * - ``and``
      - True if both conditions are true
      - ``x > 5 and x < 10``
      - Checks if ``x`` is between ``5`` and ``10`` (both conditions must hold)
    * - ``or``
      - True if at least one condition is true
      - ``x < 5 or x > 10``
      - Checks if ``x`` is either less than ``5`` or greater than ``10`` (either condition suffices)
    * - ``not``
      - Inverts a condition (True if the condition is false)
      - ``not (x == 5)``
      - True when ``x`` is not equal to ``5``

Example Usage
-------------

Let's try this out with a simple example. Suppose we want to check if a number is positive, negative, or zero:

.. code-block:: python

    # get a number from a user and convert it to a float
    number = float(input("Enter a number: "))

    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

We could have also have checked if the number was zero first, it would give you the same result!

Now let's build a more complicated condition. Python is quite nice in that it reads quite close to English. See if you can understand what this condition is checking for:

.. code-block:: python

    age = int(input("Enter your age: "))

    if (age >= 18 and age <= 65) or (age % 2 == 0):
        print("You met the condition!")
    else:
        print("Suck it up, buttercup.")

.. dropdown:: Click to show answer 

    This condition checks if the user is either between 18 and 65 years old (inclusive) or if their age is an even number. If either of these conditions is true, it prints "You met the condition!" Otherwise, it prints "Suck it up, buttercup."


Practice Problem
----------------

Now that you've learned about conditions, try applying this knowledge in the practice problem found in part three of the `greeting <../problems/greeting.html>`_ problem in the Problems section.