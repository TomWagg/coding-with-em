Inheritance
===========

We inherit all sorts of things from our parents, even beyond a bad sense of humour! One particular trait that is inherited from parents is blood type. Blood type is determined by the alleles we inherit from our parents. There are three main alleles for blood type: A, B, and O. The A and B alleles are dominant, while the O allele is recessive.

These alleles determine your genotype, which in turn determines your blood type (phenotype). Here are the possible genotypes and their corresponding blood types:

- AA or AO: Blood type A
- BB or BO: Blood type B
- AB: Blood type AB
- OO: Blood type O

Let's look at an example. If one parent has blood type A (genotype AO) and the other parent has blood type B (genotype BO), their children could have the following genotypes and blood types:

- AB: Blood type AB
- AO: Blood type A
- BO: Blood type B
- OO: Blood type O

This means that the children could have any of the four blood types: A, B, AB, or O. The specific blood type of each child would depend on which alleles they inherit from their parents.

Problem overview
----------------

We're going to determine how the statistics of a population's genotypes and phenotypes change over generations. This can inform us also about who can donate blood to whom in a population. But we'll split this problem into a couple of parts and build up to it.

Part 1: Genotype to Phenotype
-----------------------------

Let's warm up by implementing the ``genotype_to_phenotype`` function. This function will take a genotype (a string representing the alleles) and return the corresponding blood type (phenotype).

The function should check that the input genotype is valid (i.e., it should be one of "AA", "AO", "BB", "BO", "AB", or "OO"). If the genotype is valid, the function should return the corresponding blood type. If the genotype is invalid, the function should return "Invalid genotype".

Here's some example usage of the function:

.. code-block:: python

    print(genotype_to_phenotype("AA"))  # Output: A
    print(genotype_to_phenotype("BO"))  # Output: B
    print(genotype_to_phenotype("AB"))  # Output: AB
    print(genotype_to_phenotype("OO"))  # Output: O
    print(genotype_to_phenotype("AC"))  # Output: Invalid genotype


