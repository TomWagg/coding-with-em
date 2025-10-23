mutations
=========

.. figure:: ../../_static/mutation_breakup.png
    :alt: Two DNA strands breaking up
    :align: center
    :width: 500px

    It's not you, it's not me, it's just mutations.

In `the previous problem <genome.html>`_, we learned about genomes, nucleotide sequences, and how ribosomes
build proteins from those sequences. In this problem, we'll consider how mutations can cause things to go
wrong when trying to build those proteins.

Concepts
--------

First, let's review some key concepts (that I may or may not have only just learned myself!). We're can think
about two different types of mutations that can occur in a nucleotide sequence:

- **Point mutations**: A single nucleotide is changed to a different nucleotide. For example, an "A" might be changed to a "G".
- **Frame-shift mutations**: One or more nucleotides are added to or removed from the sequence. For example, an "A" might be inserted into the sequence, or a "T" might be deleted.

.. figure:: ../../_static/point_vs_frame_shift.png
    :alt: Point mutation vs frame-shift mutation
    :align: center
    :width: 600px

    Some mutations have bigger effects than others.

You can imagine that a point mutation will have a smaller effect on the resulting protein than a frame-shift
mutation, since the latter will change the reading frame of all subsequent codons.

We can further classify mutations based on their effect on the resulting protein:

- **Silent mutations**: The mutation does not change the amino acid that is produced. For example, both "GAA"and "GAG" code for the amino acid glutamic acid, so a mutation from "GAA" to "GAG" would be silent.
- **Missense mutations**: The mutation changes the amino acid that is produced. For example, a mutation from "GAA" to "GAC" would change the amino acid from glutamic acid to aspartic acid.
- **Nonsense mutations**: The mutation changes a codon to a stop codon, causing the protein to be truncated. For example, a mutation from "GAA" to "TAA" would change the codon to a stop codon.

.. admonition:: Required humour

    You should now check your learning by looking at the first image again now you know what a nonsense mutation is! If you don't laugh, you must not have understood the concept properly, there's no other explanation.

For the purposes of this problem, we'll only be thinking about point mutations, but if you're keen there's an extra credit section at the end where you can try to handle frame-shift mutations as well.

Your task
---------

Imagine you have a reference nucleotide sequence (the "correct" sequence) from some perfect organism that has no mutations. Next you have a second nucleotide sequence from an organism that may have some mutations relative to the reference sequence.

Part 1: Find the mutations
--------------------------

First, implement ``find_point_mutations(reference, mutated)`` which takes in two nucleotide sequences (strings) and returns a list of locations (0-indexed) where the point mutations occur. You can assume that both sequences are the same length and only differ by point mutations (i.e., no insertions or deletions). You can also assume that the sequences only contain the characters "A", "C", "G", and "T".

Here are some test cases to get you started:

.. code-block:: python

    find_point_mutations("ACGT", "ACGT")  # should return []
    find_point_mutations("ACGT", "AGGT")  # should return [1]
    find_point_mutations("ACGT", "TGCA")  # should return [0, 1, 2, 3]


Part 2: Classify the mutations
------------------------------

Now the real question is: what effect do those mutations have on the resulting protein? To answer this, implement ``classify_mutations(reference, mutated)`` which takes in two nucleotide sequences (strings) and returns a list of tuples, where each tuple contains the index of the mutation and its classification ("silent", "missense", or "nonsense").

You can use the genetic code table from the previous problem to determine the amino acids produced by each codon.

**To simplify things**, the sequences that you receive will always start with a start codon ("ATG") and end with a stop codon ("TAA", "TAG", or "TGA"), and the length of the sequences will always be a multiple of 3. There will also only be point mutations (no insertions or deletions), and only one mutation will occur per codon.

Recall that silent mutations do not change the amino acid, missense mutations change the amino acid, and nonsense mutations change a codon to a stop codon.

Here are some test cases to get you started:

.. code-block:: python

    reference = "ATGGAGCCATAA"

    classify_mutations(reference, "ATGGAGCCATAA")   # should return []
    classify_mutations(reference, "AGGGAGCCGTAA")   # should return [(1, "missense")]
    classify_mutations(reference, "ATGGAGCCCTAA")   # should return [(8, "silent")]
    classify_mutations(reference, "ATGTAGCCCTAA")   # should return [(3, "nonsense"), (8, "silent")]


Part 3: (Extra credit) Handle frame-shift mutations
---------------------------------------------------

TODO