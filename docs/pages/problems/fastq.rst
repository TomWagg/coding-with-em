fastq
=====

*Difficulty*: ★★★☆☆

.. figure:: ../../_static/fastq.png
   :align: center
   :width: 600px

   That line is certainly move towards the sequencing machine quickly...

In this problem we're going to think about interacting with files with Python. Since genome data is often stored in FASTQ format, we'll use a FASTQ file for this exercise.

The `FASTQ format <https://en.wikipedia.org/wiki/FASTQ_format>`_ is a text-based format for storing both a biological sequence (usually nucleotide sequence) and its corresponding quality scores. Each sequence in a FASTQ file is represented by four lines that look like this

.. code-block::

    @SEQ_ID
    GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT
    +
    !''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65

The first line is an ID that uniquely identifies the sequence that it describes. The second line is the raw sequence letters. The third line is a separator (often just a plus sign). The fourth line encodes the quality scores for the sequence in line 2, with each character representing the quality of the corresponding base in the sequence.

The quality values are encoded using ASCII characters. To convert a character to its corresponding quality score, you subtract 33 from its ASCII value. For example, the character 'I' has an ASCII value of 73, so its quality score would be 73 - 33 = 40.

Testing your code
-----------------

You can test your code by running ``python problems/fastq.py`` from the root of the repository. This will run a few tests on your code to make sure it is working as expected.

Part 1: Writing a file parser
-----------------------------

The first thing we need to do is write a function that can parse a FASTQ file and convert its contents into a more manageable data structure. Specifically, we want to convert the FASTQ file into a list of dictionaries, where each dictionary represents a single sequence entry with the following keys:

- ``id``: The sequence identifier (from line 1)
- ``sequence``: The raw sequence letters (from line 2)
- ``quality``: A list of quality scores (from line 4, converted to integers)

With this in mind, implement the function ``parse_fastq(file_path)`` in ``problems/fastq.py`` that takes the path to a FASTQ file as input and returns the list of dictionaries as described above. If no file is found at the given path, the function should raise a ``FileNotFoundError`` and explain to the user that the file could not be found.

Here's an example of how the output should look for a FASTQ file with a single entry:

.. code-block:: python

    data = parse_fastq('example.fastq')
    print(data)

    # output looks like this:
    # [
    #     {
    #         'id': 'SEQ_ID',
    #         'sequence': 'GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT',
    #         'quality': [40, 39, 38, 37, ...]  # list of quality scores as integers
    #     }
    # ]

Part 2: A question of quality
-----------------------------

Since these nice sequencer people are going to all of the trouble of reporting quality scores for each base in the sequence, we should probably make use of that information. Implement the function ``filter_by_quality(data, threshold)`` in ``problems/fastq.py`` that takes two arguments:
- ``data``: The list of dictionaries returned by ``parse_fastq``
- ``threshold``: An integer quality score threshold

The function should return a new list of dictionaries that only includes those sequences where every base in the sequence has a quality score greater than or equal to the given threshold.

Part 3: Protein confusion
-------------------------

This method of filtering will of course get rid of any particularly aggregious sequences, but you can imagine scenarios where the average quality of a sequence is high, but there are still a few low-quality bases scattered throughout.

Let's think about how this might change what proteins we predict from these sequences. Luckily, in an earlier problem we already wrote a function ``find_proteins(sequence)`` that can find all of the proteins encoded by a given DNA sequence so that bit's easy. Now, let's make a dramatic assumption that for some reason "C" nucleotides are always hard to read, so if we find a low quality score (below some threshold) at a position in the sequence, it's possible we should have read a "C" there instead.

Implement the function ``protein_variations(data, average_threshold, point_threshold)`` in ``problems/fastq.py`` that takes three:

- ``data``: The list of dictionaries returned by ``parse_fastq``
- ``average_threshold``: An integer quality score threshold for average quality
- ``point_threshold``: An integer quality score threshold for individual bases

First, the function uses ``filter_by_quality`` to filter the sequences by average quality using ``average_threshold``. Then, for each remaining sequence, use ``find_proteins`` to predict the protein content of the sequence as-is. Next, for each base in the sequence that has a quality score below ``point_threshold``, create a modified version of the sequence where that base is changed to "C" (if it isn't already "C"), and use ``find_proteins`` to predict the protein content of this modified sequence.

Three things could happen here: either the modified sequence will produce *identical* proteins, the same *number* of proteins, or it will produce a *different* number of proteins (because a start/end codon got created or destroyed). Because of this you should track two different things:

- ``diff_count_seqs``: A list of tuples, where each tuple contains the sequence ID, the original number of proteins, and the modified number of proteins
- ``same_count_seqs``: A list of tuples, where each tuple contains the sequence ID and a list where each element is the number of amino acids that are different in each protein in the modified sequence compared to the original sequence
- ``high_quality_sequences``: A list of sequence IDs that produce identical proteins even after modification

If there's a different number of proteins, update ``diff_count_seqs``. If there's the same number of proteins, compare each protein in the modified sequence to the corresponding protein in the original sequence and count how many amino acids are different. If there are any differences, update ``same_count_seqs``. If there are no differences at all, add the sequence ID to ``high_quality_sequences``.

.. Bonus: Tom's binary soap box
.. ----------------------------

.. Nope, not that kind of binary. I'm not talking about stars, I'm talking about computers. Specifically, I'm talking about how computers store text. I am still baffled as to why FASTQ files use ASCII characters to encode information when computers are perfectly capable of storing binary data directly. I would like to prove that it is both faster, and more space efficient, to store FASTQ data in binary format - specifically HDF5 format.

.. I'm not even going to make you do it, I am simply here to prove my point lol. If I do the following:

.. .. code-block:: python

..     import time
..     import h5py
..     import os

..     folder = "../files/"
..     fastq_path = folder + 'large.fastq'
..     h5_path = folder + 'large.h5'

..     # Measure ASCII file size and read time
..     ascii_size = os.path.getsize(fastq_path)
..     start_time = time.time()
..     data = parse_fastq(fastq_path)
..     ascii_read_time = time.time() - start_time

..     # Convert to HDF5 and measure size and read time
..     with h5py.File('h5_path', 'w') as f:
..         ids = [entry['identifier'] for entry in data]
..         sequences = [entry['sequence'] for entry in data]
..         qualities = [entry['quality'] for entry in data]
..         comments = [entry['comment'] for entry in data]

..         f.create_dataset('ids', data=ids)
..         f.create_dataset('sequences', data=sequences)
..         f.create_dataset('qualities', data=qualities)
..         f.create_dataset('comments', data=comments)

..     hdf5_size = os.path.getsize(h5_path)
..     start_time = time.time()
..     with h5py.File(h5_path, 'r') as h5f:
..         ids = h5f['ids'][:]
..         sequences = h5f['sequences'][:]
..         qualities = h5f['qualities'][:]
..         comments = h5f['comments'][:]
..     hdf5_read_time = time.time() - start_time

..     print(f'ASCII size: {ascii_size} bytes, read time: {ascii_read_time} seconds')
..     print(f'HDF5 size: {hdf5_size} bytes, read time: {hdf5_read_time} seconds')
