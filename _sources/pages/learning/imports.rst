Imports
=======

In Python, you can use imports to bring in code from other modules and libraries. This allows you to reuse code and organize your programs better, or use code written by others.

Importing a module
------------------

To import a module, you use the ``import`` statement followed by the name of the module you want to import. For example, to import the built-in ``math`` module, you would write:

.. code-block:: python

    import math

By built-in, we mean that the module comes pre-installed with Python, so you don't need to install anything extra to use it. You can then use functions and constants defined in the ``math`` module by prefixing them with ``math.``. For example:

.. code-block:: python

    print(math.sqrt(16))  # Output: 4.0
    print(math.pi)        # Output: 3.141592653589793


Importing specific functions or variables
-----------------------------------------

Sometimes, you might only need a specific function or variable from a module. In that case, you can use the ``from`` keyword to import just what you need. For example, to import only the ``sqrt`` function from the ``math`` module, you would write:

.. code-block:: python

    from math import sqrt

    print(sqrt(25))  # Output: 5.0

You can also import multiple specific items by separating them with commas:

.. code-block:: python

    from math import sqrt, pi

    print(sqrt(36))  # Output: 6.0
    print(pi)        # Output: 3.141592653589793


Importing with an alias
-----------------------

You can also give a module or function an alias (a different name) when you import it using the ``as`` keyword. This can be useful to shorten long module names or avoid naming conflicts. For example:

.. code-block:: python

    import random as rnd

    print(rnd.randint(1, 10))

This imports the ``random`` module but allows you to refer to it as ``rnd`` in your code.

You can also alias specific functions:

.. code-block:: python

    from math import sqrt as square_root

    print(square_root(49))  # Output: 7.0

Importing all items from a module
---------------------------------

While not generally recommended due to potential naming conflicts, you can import everything from a module using the asterisk (*) wildcard:

.. code-block:: python

    from math import *

    print(sin(pi / 2))  # Output: 1.0
    print(cos(0))       # Output: 1.0

This imports all functions and variables from the ``math`` module directly into your namespace, so you can use them without the ``math.`` prefix. However, be cautious when using this approach, as it can lead to confusion if different modules have functions or variables with the same name.


Importing your own modules
--------------------------

You can also create your own modules by saving Python code in a file with a ``.py`` extension. You can then import that file as a module in another Python script. For example, if you have a file named ``my_module.py`` with the following content:

.. code-block:: python
    :caption: my_module.py

    def greet(name):
        return f"Hello, {name}!"

You can import and use it in another script like this:

.. code-block:: python
    :caption: other.py

    from my_module import greet

    print(greet("Emily"))

You can imagine how this can help you organize larger programs by splitting code into multiple files and importing only what you need. This is extended further with packages, which are collections of modules organized in directories, but that's a topic for another time.

That's a brief overview of how imports work in Python! They are a powerful feature that helps you organize and reuse code effectively.
