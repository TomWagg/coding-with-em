genome
======

A person's genome can be written as a sequence of nucleotides, consisting of four different ones, Adenine (A), Thymine (T), Guanine (G), Cytosine (C). This means that any particular chunk of genome might look something like this:

    GATCTCCATGTCAAACTCTATCCATTAGATCTCTA

In this problem, we're going to develop some code to explore a person's genome.

All of your code will be written in ``problems/genome.py`` and running the script will test your code.

Part one
--------

Your first task is to determine the statistics of different nucleotides within a genome. Implement the ``nucleotide_stats`` function, which takes ``genome``, which is a string of nucleotides, as an argument.

Write some code in this function such that the function returns a dictionary with the counts of each nucleotide. Here are some test cases for you:

.. code-block:: python

    print(nucleotide_stats("ATGC"))         # {"A": 1, "T": 1, "G": 1, "C": 1}
    print(nucleotide_stats("ATGCTGGC"))     # {"A": 1, "T": 2, "G": 3, "C": 2}
    print(nucleotide_stats("AAAAAAAA"))     # {"A": 8, "T": 0, "G": 0, "C": 0}


Part two
--------

Now let's make things a little more complicated. Sets of three nucleotides constitute a "codon". Implement the ``codon_stats`` function, which takes ``genome``, which is a string of nucleotides, as an argument.


Write some code in this function such that the function returns a dictionary with the counts of each *unique codon*.

.. code-block:: python

    print(codon_stats("ATGC"))         # {"ATG": 1, "TGC": 1}
    print(codon_stats("ATGCTGGC"))     # {"ATG": 1, "TGC": 1, "GCT": 1, "CTG": 1, "TGG": 1, "GGC": 1} 
    print(codon_stats("AAAAAAAA"))     # {"AAA": 6}

Part three
----------

I'm not sure this part is actually useful in biology, but it *is* fun to think about. Let's think about palindromes, which are words that are spelt the same way forwards and backwards - think racecar, hannah, tacocat!

Your task, should you choose to accept it (...which you have to, this is your homework) is to implement the function ``count_palindromes(genome, length)``, which takes a string of nucleotides (``genome``) and an integer ``length`` as arguments. This function should return the number of palindromes that are exactly ``length`` characters long.

Here are some test cases for you

.. code-block:: python

    # this should output 3, coming from (ATA, CTC, TCT)
    print(count_palindromes("ATAATCGTCCTCT", 3))

    # this should output 2, coming from (TAAT, TCCT)
    print(count_palindromes("ATAATCGTCCTCT", 4))


Part four
---------

.. margin::

    If you think about it, given that your ribosomes know how to do this, you should find this part easy! If you're struggling, consider meditation to communicate with your inner self.

Finally, let's consider something that your body (specifically, the ribosomes in your cells) has to do constantly. Not every part of your genome is actually coding for specific proteins. Lots of it is useless! This is why some mutations have no effect on you.

Your body has some specific tags that track when a protein is being coded for. Everything contained within a start and stop codon will be used to make a protein. The "start" codon is "ATG", while the end codon could be any of "TAA", "TAG", and "TGA", whichever comes first.

.. margin::

    In reality, coding sequences have more requirements than this, but this gives us a good approximation.

Your ribosomes will scan across from the start to the end codon (clever little fellas), reading chunks of three nucleotides at a time, excluding the end codon. For a coding sequence to be valid, there must be at least codons within it, which can include the start codon. For example "ATGTAG" is not valid, because it only contains "ATG". "ATGATAG" is also not valid, because it contains "ATG" and "ATA", but the "ATA" would eat into the end codon. Instead, something like "ATGGAATAG" would be valid, since it contains "ATG", "GAA" and the end codon. This could have a length of 2 codons. In short, you should ensure that the number of nucleotides between your start and end sequence is a multiple of three!

Your task in this part is to identify the nucleotides that are coding for proteins within your input. Implement the function ``find_proteins(genome)``, which takes a string of nucleotides (``genome``) as an argument, and returns a list with the number of codons contained in each sequence in the genome. Don't include invalid sequences in this list.

Here are some test cases for you

.. code-block:: python

    # expected output: [2]
    print(find_proteins("ATGAGGTAG"))

    # expected output: [], since it's invalid
    print(find_proteins("ATGCCTAG"))

    # expected output: [2, 3]
    print(find_proteins("ATGAAATAGAGGCATGGACACATAACT"))

