CODON_TO_AMINO_ACID = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
    'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W'
}


def find_point_mutations(reference, mutated):
    """Identify point mutations between reference and mutated sequences.

    Parameters
    ----------
    reference : str
        The original reference sequence with no mutations.
    mutated : str
        The mutated sequence potentially containing point mutations.

    Returns
    -------
    mutation_locations : list
        A list of indices where point mutations occur.
    """
    return []


def classify_point_mutations(reference, mutated):
    """Classify point mutations as silent, missense, or nonsense.

    This function makes several assumptions:

        - The reference and mutated sequences are of the same length.
        - Mutations are single nucleotide changes (point mutations).
        - Only one mutation occurs per codon.
        - The sequences start at the beginning of a codon (i.e., index 0 is the start of a codon).
        - The end of the sequence does not contain partial codons and ends with an end codon.

    Parameters
    ----------
    reference : str
        The original reference nucleotide sequence.
    mutated : str
        The mutated nucleotide sequence.

    Returns
    -------
    classifications : list of tuples
        A list of tuples where each tuple contains the index of the mutation
        and its classification ("silent", "missense", or "nonsense"). e.g. [(6, "missense"), (15, "nonsense")]
    """
    return []


def needleman_wunsch(s1, s2, match=1, mismatch=-1, gap=-2):
    """Perform Needleman-Wunsch alignment of two sequences.

    This algorithm performs global alignment of two sequences using dynamic programming. The general method
    is as follows:
        1. Create a scoring matrix and a traceback matrix.
        2. Fill in the scoring matrix based on match, mismatch, and gap penalties.
        3. Trace back through the traceback matrix to get the aligned sequences.
        4. Return the aligned sequences and the alignment score.

    In more detail, the scoring matrix is filled in such that each cell represents the best score achievable
    for aligning the prefixes of the two sequences up to that point. The traceback matrix records the
    direction from which the best score was derived (diagonal, up, or left), which is then used to reconstruct
    the optimal alignment.

    At each step, the algorithm considers three possible scenarios: a match/mismatch (diagonal move),
    a gap in the first sequence (up move), or a gap in the second sequence (left move). The maximum score
    from these scenarios is chosen for each cell in the scoring matrix. Based on the chosen maximum score,
    the corresponding direction is recorded in the traceback matrix.

    Parameters
    ----------
    s1 : str
        The first sequence to align
    s2 : str
        The second sequence to align
    match : int, optional
        Score for a match, should be positive, by default 1
    mismatch : int, optional
        Score for a mismatch, should be negative, by default -1
    gap : int, optional
        Score for a gap, should be negative, by default -2

    Returns
    -------
    aligned_s1 : str
        The aligned version of s1, with gaps represented by '-'
    aligned_s2 : str
        The aligned version of s2, with gaps represented by '-'
    """
    return s1, s2


def detect_mutations(reference, mutated):
    """Detect both point and frameshift mutations between reference and mutated sequences.

    Apply the Needleman-Wunsch algorithm to align the two sequences, then analyze the alignment
    to identify point mutations and frameshift mutations (insertions and deletions).

    This function returns a dictionary containing:
        - The alignment of the two sequences.
        - A list of point mutations, each represented as a tuple (position, reference_nucleotide, mutated_nucleotide).
        - A list of frameshift mutations, each represented as a dictionary with keys 'type', 'seq', and 'length'.

    Parameters
    ----------
    reference : str
        The original reference nucleotide sequence.
    mutated : str
        The mutated nucleotide sequence.

    Returns
    -------
    mutations : dict
        A dictionary with keys 'alignment', 'point_mutations', and 'frameshift_mutations'.
    """
    aligned_ref, aligned_mut = needleman_wunsch(reference, mutated)
    mutations = {
        "alignment": (aligned_ref, aligned_mut),
        "point_mutations": [],
        "frameshift_mutations": []
    }
    return mutations


#############################################################
#############################################################
########################## STOP! ############################
##### You don't need to change anything below this line #####
#############################################################
#############################################################
#############################################################

import random
from pathlib import Path
import sys

sys.path.insert(0, str((Path(__file__).resolve().parent.parent / "solutions/")))
import mutations_solution as sol

# define ansi red and green for terminal output
RED, GREEN, RESET = "\033[91m", "\033[92m", "\033[0m"


def random_genome(length):
    stats = {
        "A": random.randint(0, length),
        "G": random.randint(0, length),
        "T": random.randint(0, length),
        "C": random.randint(0, length),
    }
    genome = "".join([k * stats[k] for k in stats])
    genome_chars = [c for c in genome]
    random.shuffle(genome_chars)
    genome = "".join(genome_chars)
    genome = genome[:length]

    # get rid of accidental start/stop codons
    NUCLEOTIDES = ['A', 'T', 'C', 'G']
    BAD_CODONS = ["ATG", "TAA", "TAG", "TGA"]
    for i in range(0, len(genome) - 2):
        codon = genome[i:i + 3]
        if codon in BAD_CODONS:
            candidate_codon = codon
            # ensure adding a new codon doesn't create another bad codon (either here, two places back, or one place back, where each codon has 3 places)
            while (candidate_codon in BAD_CODONS
                   or (i >= 2 and genome[i - 2:i] + candidate_codon[0] in BAD_CODONS)
                   or (i >= 1 and genome[i - 1:i] + candidate_codon[0:2] in BAD_CODONS)
            ):
                candidate_codon = ''.join(random.choices(NUCLEOTIDES, k=3))
            genome = genome[:i] + candidate_codon + genome[i + 3:]

    for i in range(len(genome) - 2):
        assert genome[i:i + 3] not in BAD_CODONS, "Failed to remove all bad codons, shout at Tom!"

    return genome


def mutate_genome(genome):
    # add point mutations to the genome, but only with one per codon, assume genome starts with start codon and ends with stop codon
    NUCLEOTIDES = ['A', 'T', 'C', 'G']
    genome_list = list(genome)
    for i in range(3, len(genome) - 3, 3):
        if random.random() < 0.1:  # 10% chance of mutation per codon
            codon_pos = random.randint(0, 2)
            original_nucleotide = genome_list[i + codon_pos]
            new_nucleotide = original_nucleotide
            while new_nucleotide == original_nucleotide:
                new_nucleotide = random.choice(NUCLEOTIDES)
            genome_list[i + codon_pos] = new_nucleotide
    return ''.join(genome_list)


def main():
    N_TESTS = 100
    # random_genome(12)
    # exit()
    genomes = [
        "ATG" + random_genome(12) + "TAA" for _ in range(N_TESTS // 3)
    ] + [
        "ATG" + random_genome(123) + "TAG" for _ in range(N_TESTS // 3)
    ] + [
        "ATG" + random_genome(1236) + "TAA" for _ in range(N_TESTS // 3)
    ]

    mutated_genomes = [mutate_genome(genome) for genome in genomes]

    part1_passed = True
    for genome, mutated in zip(genomes, mutated_genomes):
        if not part1_passed:
            break
        student = find_point_mutations(reference=genome, mutated=mutated)
        answer = sol.find_point_mutations(reference=genome, mutated=mutated)
        if len(student) != len(answer) or any(student[i] != answer[i] for i in range(len(answer))):
            part1_passed = False
            print(f"{RED}Part 1 test failed: genome={genome}, mutated={mutated}, expected {answer}, got {student}{RESET}")

    if part1_passed:
        print(f"{GREEN}Part 1 passed!{RESET}")
    else:
        print(f"{RED}Part 1 failed :({RESET}")

    part2_passed = True
    for genome, mutated in zip(genomes, mutated_genomes):
        if not part2_passed:
            break
        student = classify_point_mutations(reference=genome, mutated=mutated)
        answer = sol.classify_point_mutations(reference=genome, mutated=mutated)
        if len(student) != len(answer) or any(student[i] != answer[i] for i in range(len(answer))):
            part2_passed = False
            print(f"{RED}Part 2 test failed: genome={genome}, mutated={mutated}, expected {answer}, got {student}{RESET}")

    if part2_passed:
        print(f"{GREEN}Part 2 passed!{RESET}")
    else:
        print(f"{RED}Part 2 failed :({RESET}")

if __name__ == "__main__":
    main()
