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


def nucleotide_stats(genome):
    """Count up the nucleotide stats in a genome

    Parameters
    ----------
    genome : `str`
        A string of nucleotides, you can assume every character is one of "ATGC"

    Returns
    -------
    stats : `dict`
        A dictionary of the counts of each nucleotide, e.g. {"A": 1, "T": 1, "G": 1, "C": 1}
    """
    return {}


def codon_stats(genome):
    """Count up the codon stats in a genome

    Parameters
    ----------
    genome : `str`
        A string of nucleotides, you can assume every character is one of "ATGC"

    Returns
    -------
    stats : `dict`
        A dictionary of the counts of each codon,
        e.g. {"ATG": 1, "TGC": 1, "GCT": 1, "CTG": 1, "TGG": 1, "GGC": 1} 
    """
    return {}


def count_palindromes(genome, length):
    """Count the number of palindromes of a given length in a genome

    Parameters
    ----------
    genome : `str`
        A string of nucleotides, you can assume every character is one of "ATGC"
    length : `int`
        Length of palindrome to search for

    Returns
    -------
    count : `int`
        Total number of palindromes of correct length in genome
    """
    return 0


def find_proteins(genome):
    """Find the proteins encoded by a genome.

    Parameters
    ----------
    genome : `str`
        A string of nucleotides, you can assume every character is one of "ATGC"

    Returns
    -------
    proteins : `list` of `str`
        A list of the valid proteins encoded by the genome
    """
    return []


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
import genome_solution as sol

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
    return genome[:length]


def insert_open_reading_frames(genome):
    # get rid of accidental start/end codons
    genome = genome.replace("ATG", "CCC").replace("TAA", "CCC").replace("TAG", "CCC").replace("TGA", "CCC")

    # track location and number of insertions
    i = 0
    insertions = 0

    # loop until we reach the end of the genome
    while i < len(genome):
        # pick a random start location for the coding sequence
        start_loc = random.randint(i, len(genome))

        # pick a random length for the coding sequence (in codons)
        length = random.randint(1, 10)
        end_loc = start_loc + length * 3

        # ensure we don't go past the end of the genome
        if end_loc + 3 >= len(genome):
            break

        # otherwise, insert an ATG at the start location and a random end codon at the end location
        # also add a C before the start codon and after the stop codon to avoid accidental start/stop codons
        genome = (
            genome[:start_loc]
            + "C" + "ATG"
            + genome[start_loc:end_loc]
            + random.choice(["TAA", "TAG", "TGA"])
            + "C" + genome[end_loc + 3:]
        )

        # move index forward quite a lot to avoid overlapping coding sequences
        i = end_loc + 10

        # increment number of insertions
        insertions += 1

    return genome, insertions


def main():
    N_TESTS = 100
    test_cases = [
        insert_open_reading_frames(genome=random_genome(10))[0] for _ in range(N_TESTS // 3)
    ] + [
        insert_open_reading_frames(genome=random_genome(100))[0] for _ in range(N_TESTS // 3)
    ] + [
        insert_open_reading_frames(genome=random_genome(10000))[0] for _ in range(N_TESTS // 3)
    ]
    palindrome_lengths = [random.randint(3, 10) for _ in range(N_TESTS)]

    for part, func, answer_fun in zip([1, 2], [nucleotide_stats, codon_stats],
                                      [sol.nucleotide_stats, sol.codon_stats]):
        part_passed = True
        for genome in test_cases:
            if not part_passed:
                break
            student, answer = func(genome=genome), answer_fun(genome=genome)
            for key in answer:
                if key not in student or student[key] != answer[key]:
                    part_passed = False
                    print(f"{RED}Part {part} test failed: genome={genome}, expected {answer}, got {student}{RESET}")
                    break

        if part_passed:
            print(f"{GREEN}Part {part} passed!{RESET}")
        else:
            print(f"{RED}Part {part} failed :({RESET}")

    part3_passed = True
    for genome, length in zip(test_cases, palindrome_lengths):
        if not part3_passed:
            break
        student = count_palindromes(genome=genome, length=length)
        answer = sol.count_palindromes(genome=genome, length=length)
        if student != answer:
            part3_passed = False
            print(f"{RED}Part 3 test failed: genome={genome}, palindrome length={length}, expected {answer}, got {student}{RESET}")

    if part3_passed:
        print(f"{GREEN}Part 3 passed!{RESET}")
    else:
        print(f"{RED}Part 3 failed :({RESET}")

    part4_passed = True
    for genome in test_cases:
        if not part4_passed:
            break
        student = find_proteins(genome=genome)
        answer = sol.find_proteins(genome=genome)
        if len(student) != len(answer) or any(student[i] != answer[i] for i in range(len(answer))):
            part4_passed = False
            print(f"{RED}Part 4 test failed: genome={genome}, expected {answer}, got {student}{RESET}")

    if part4_passed:
        print(f"{GREEN}Part 4 passed!{RESET}")
    else:
        print(f"{RED}Part 4 failed :({RESET}")


if __name__ == "__main__":
    main()
