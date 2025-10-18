Files
=====

It's very useful to be able to read from and write to files in Python. This allows you to save data, configurations, or any other information that your program might need to persist between runs.

We'll just talk about text files here, but Python can also handle binary files (like images or executables) in a similar way.

Opening a file
--------------

To work with a file, you first need to open it using the built-in ``open()`` function. This function takes at least one argument: the name of the file you want to open. You can also specify the mode in which you want to open the file (e.g., for reading, writing, or appending).

.. code-block:: python

    file = open("example.txt", "r")  # Open for reading
    file = open("example.txt", "w")  # Open for writing (will overwrite)
    file = open("example.txt", "a")  # Open for appending

Opening a file this way requires you to manually close it later using ``file.close()``. However, a better practice is to use a ``with`` statement, which automatically takes care of closing the file for you:

.. code-block:: python

    with open("example.txt", "r") as file:
        # do stuff with the file here

Here, the file is only open during the indented block under the ``with`` statement.

Reading from a file
-------------------

To read the contents of a file, you can use methods like ``read()``, ``readline()``, or ``readlines()``. Here's an example of reading the entire content of a file:

.. code-block:: python

    with open("example.txt", "r") as file:
        for line in file:
            print(line)

This will print each line of the file to the console. We could also loop over each character in each line if we wanted to:

.. code-block:: python

    with open("example.txt", "r") as file:
        for line in file:
            for char in line:
                print(char)

Writing to a file
-----------------

To write to a file, you can open it in write (``"w"``) or append (``"a"``) mode. Write mode will overwrite the existing content, while append mode will add new content to the end of the file.

.. code-block:: python

    with open("example.txt", "w") as file:
        file.write("Hello, world!\n")
        file.write("This is a new line.\n")

You can also use the ``writelines()`` method to write multiple lines at once:

.. code-block:: python

    lines = ["First line.\n", "Second line.\n", "Third line.\n"]
    with open("example.txt", "a") as file:
        file.writelines(lines)
