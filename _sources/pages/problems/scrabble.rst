scrabble
========

*Difficulty*: ★★★★★

.. figure:: ../../_static/scrabble.png
    :align: center

    Counting *and* spelling, oh my!

Let's take a break from genetics for a moment and think about Scrabble instead! In this problem we're going to write some code that scores potential Scrabble words.

Testing your code
-----------------

You can test your code by running ``python problems/scrabble.py`` from the root of the repository. This will run a few tests on your code to make sure it is working as expected.

Part 1: Scoring words
---------------------

The first thing we need to do is write a function that can score Scrabble words. We're not going to worry about board position or anything fancy like that, just the raw score of the word based on the letter values. Implement the function ``score_word(word)`` in ``problems/scrabble.py`` that takes a single word as input and returns its Scrabble score as an integer.

I've included a Python dictionary called ``LETTER_SCORES`` in ``problems/scrabble.py`` that maps each letter to its corresponding Scrabble score. You can use this dictionary to look up the score for each letter.

Part 2: Finding the best word
-----------------------------

Now that we can score individual words, let's write a function that can find the highest scoring word given a list of 7 letters (our Scrabble rack). Implement the function ``best_word(letters, word_file)`` in ``problems/scrabble.py`` that takes two arguments:

- ``letters``: A string of 7 letters representing the player's Scrabble rack
- ``word_file``: The path to a text file containing a list of valid words (one word per line)

The function should return a tuple containing the highest scoring word that can be formed with the given letters and its score. If no valid words can be formed, the function should return ``('', 0)``.

If multiple words have the same highest score, return the one that comes first alphabetically.

Part 3: Handling blanks
-----------------------

.. margin::

    One of the rare occasions where "drawing a blank" is a good thing!

In Scrabble, players can also have blank tiles that can represent any letter but have no point value. Let's modify our ``best_word`` function to handle blank tiles. Update the function so that it can accept a string of 7 characters where some of the characters may be underscores ('_') representing blank tiles.

Part 4: Spellcheck
------------------

*Disclaimer: This part and the next are directly inspired by CS50's "speller" problem set.*

.. figure:: ../../_static/bill_cheats.png
    :align: center

    Shakespeare often struggled with the concept of following a word list...

Let's consider a different scenario. Someone provides you with a long text (e.g. the full works of Shakespeare) and they want to know how well it would perform in Scrabble. Write a function ``scrabble_score_text(text_file, word_file)`` in ``problems/scrabble.py`` that takes two arguments:

- ``text_file``: The path to a text file containing the text to be analyzed
- ``word_file``: The path to a text file containing a list of valid words (one word per line)

This function needs to do a couple of things:

- Read the list of valid words from ``word_file`` and store them in a list
- Read the text from ``text_file``, splitting words up by whitespace and newlines
- For each word in the text
    - Loop through the valid words and try to find it
        - If the word is found, add its Scrabble score to a running total
        - If the word is not found, subtract 5 points from the total as a penalty for misspelling

The function should return the total Scrabble score as an integer.

Part 5: A need for speed
------------------------

We all know the importance of acting quickly in a game of Scrabble. Given that we might be working with very large texts and dictionaries, we need to make sure our code is efficient. If you implemented the last part via brute force, this will have required searching through the full word list for every single word in the text, which has a time complexity of :math:`\mathcal{O}(n*m)` where :math:`n` is the number of words in the text and :math:`m` is the number of words in the dictionary.

Your task is now to make your code as fast as possible, with the best time complexity you can manage. This will require you to think a bit more about data structures and algorithms.

.. dropdown:: Hint for :math:`\mathcal{O}(n \log m)`
    
    Since the word list is sorted already, you could implement a binary search algorithm to check for word existence. This would reduce the time complexity of checking each word from :math:`\mathcal{O}(m)` to :math:`\mathcal{O}(\log m)`, resulting in an overall time complexity of :math:`\mathcal{O}(n \log m)` for the entire text.

.. dropdown:: Bigger hint for :math:`\mathcal{O}(n)`

    A hash map (or dictionary in Python) allows for average-case constant time complexity :math:`\mathcal{O}(1)` for lookups. By storing the valid words in a hash map, you can check for the existence of each word in the text in constant time, leading to an overall time complexity of :math:`\mathcal{O}(n)` for the entire text.

    It's up to you to decide how to hash your words, keeping in mind that I'll be timing both the loading of the word list and the scoring of the text.

    Note if you have many hash collisions, your performance may degrade towards :math:`\mathcal{O}(n*m)`, so choose your hashing strategy wisely! You could use a binary search within each hash bucket to mitigate this perhaps?

    Good luck!
