def parse_fastq(file_path):
    """Parses a FASTQ file and returns a list of dictionaries representing each sequence.

    Each dictionary contains the following keys:
    - 'identifier': The sequence identifier (without the '@' symbol)
    - 'sequence': The nucleotide sequence
    - 'quality': The quality scores as a list of integers
    - 'comment': The optional comment that comes after the identifier

    Parameters
    ----------
    file_path : str
        The path to the FASTQ file.

    Returns
    -------
    data : list of dict
        A list of dictionaries, each representing a sequence from the FASTQ file.

    Raises
    ------
    FileNotFoundError
        If the specified file does not exist.
    """
    return []


def filter_by_quality(data, threshold):
    """Filters sequences based on average quality score.

    Parameters
    ----------
    data : list of dict
        A list of dictionaries representing sequences.
    threshold : float
        The minimum average quality score to retain a sequence.

    Returns
    -------
    filtered_data : list of dict
        A list of dictionaries representing sequences that meet the quality threshold.
    """
    return []


def protein_variations(data, average_threshold, point_threshold):
    """Identifies sequences with protein variations based on quality thresholds.

    First, remove any sequences with an average quality score below average_threshold. Next, for each
    remaining sequence, find the proteins that are encoded by the sequence. If there aren't any proteins,
    skip to the next sequence.

    Copy the sequence and for any
    nucleotide position where the quality score is below point_threshold, change it to a "C". Again, find the
    proteins encoded by this modified sequence.

    If the number of proteins found in the modified sequence differs from the number found in the original
    sequence, include this sequence in the ``diff_count_seqs`` list as a tuple containing the sequence ID,
    the number of proteins in the original sequence, and the number of proteins in the modified sequence.

    If the number of proteins is the same, include this sequence in the ``same_count_seqs`` list as a tuple
    containing the sequence ID and a list, which contains the number of different amino acids found in each
    corresponding protein from the original and modified sequences.

    Parameters
    ----------
    data : list of dict
        A list of dictionaries representing sequences.
    average_threshold : float
        The minimum average quality score to consider a sequence.
    point_threshold : int
        The maximum number of low-quality points allowed in a sequence.

    Returns
    -------
    diff_count_seqs : list of tuple
        A list of tuples for sequences where the number of proteins differs after modification.
    same_count_seqs : list of tuple
        A list of tuples for sequences where the number of proteins is the same after modification.
    """
    quality_data = filter_by_quality(data, average_threshold)
    diff_count_seqs = []
    same_count_seqs = []
    high_quality_sequences = []
    return diff_count_seqs, same_count_seqs, high_quality_sequences


#############################################################
#############################################################
########################## STOP! ############################
##### You don't need to change anything below this line #####
#############################################################
#############################################################
#############################################################


from pathlib import Path
import sys
import os.path
import random

sys.path.insert(0, str((Path(__file__).resolve().parent.parent / "solutions/")))
import fastq_solution as sol

# define ansi red and green for terminal output
RED, GREEN, RESET = "\033[91m", "\033[92m", "\033[0m"


def main():
    folder = str((Path(__file__).resolve().parent.parent / "files/"))
    test_files = ["small", "medium", "large"]

    part1_passed = True
    for file in test_files:
        if not part1_passed:
            break
        file_path = os.path.join(folder, f"{file}.fastq")
        student = parse_fastq(file_path=file_path)
        answer = sol.parse_fastq(file_path=file_path)
        if len(student) != len(answer):
            part1_passed = False
            print(f"{RED}Part 1 test failed: file={file}, expected {len(answer)} sequences, got {len(student)}{RESET}")
        else:
            for i in range(len(answer)):
                if student[i]["sequence"] != answer[i]["sequence"]:
                    part1_passed = False
                    print(f"{RED}Part 1 test failed: file={file}, sequence {i} does not match expected output. Solution: {answer[i]["sequence"]}, but got {student[i]["sequence"]}.{RESET}")
                    break
                if any(student[i]["quality"][j] != answer[i]["quality"][j] for j in range(len(answer[i]["quality"]))):
                    part1_passed = False
                    print(f"{RED}Part 1 test failed: file={file}, quality scores for sequence {i} do not match expected output. Solution: {answer[i]["quality"]}, but got {student[i]["quality"]}.{RESET}")
                    break

    if part1_passed:
        print(f"{GREEN}Part 1 passed :D{RESET}")
    else:
        print(f"{RED}Part 1 failed :({RESET}")

    part2_passed = True
    for file in test_files:
        if not part2_passed:
            break
        file_path = os.path.join(folder, f"{file}.fastq")
        data = sol.parse_fastq(file_path=file_path)

        for _ in range(100):
            threshold = random.randint(0, 60)
            student = filter_by_quality(data=data, threshold=threshold)
            answer = sol.filter_by_quality(data=data, threshold=threshold)
            if len(student) != len(answer):
                part2_passed = False
                print(f"{RED}Part 2 test failed: file={file}, expected {len(answer)} sequences, got {len(student)}{RESET}")
                break

    if part2_passed:
        print(f"{GREEN}Part 2 passed :D{RESET}")
    else:
        print(f"{RED}Part 2 failed :({RESET}")

    part3_passed = True
    for file in test_files:
        if not part3_passed:
            break
        file_path = os.path.join(folder, f"{file}.fastq")
        data = sol.parse_fastq(file_path=file_path)

        for _ in range(10):
            avg_threshold = random.randint(0, 60)
            point_threshold = random.randint(0, 60)
            student = protein_variations(data=data, average_threshold=avg_threshold, point_threshold=point_threshold)
            answer = sol.protein_variations(data=data, average_threshold=avg_threshold, point_threshold=point_threshold)
            if len(student[0]) != len(answer[0]) or len(student[1]) != len(answer[1]) or len(student[2]) != len(answer[2]):
                part3_passed = False
                print(f"{RED}Part 3 test failed: file={file}, expected {len(answer[0])} diff count sequences, got {len(student[0])}; expected {len(answer[1])} same count sequences, got {len(student[1])}; expected {len(answer[2])} high quality sequences, got {len(student[2])}{RESET}")
                break

            for i in range(len(answer[0])):
                if student[0][i] != answer[0][i]:
                    part3_passed = False
                    print(f"{RED}Part 3 test failed: file={file}, diff count sequence {i} does not match expected output. Solution: {answer[0][i]}, but got {student[0][i]}.{RESET}")
                    break

            for i in range(len(answer[1])):
                if len(student[1][i][1]) != len(answer[1][i][1]) or any(student[1][i][1][j] != answer[1][i][1][j] for j in range(len(answer[1][i][1]))):
                    part3_passed = False
                    print(f"{RED}Part 3 test failed: file={file}, same count sequence {i} does not match expected output. Solution: {answer[1][i]}, but got {student[1][i]}.{RESET}")
                    break

            if any(student[2][i] != answer[2][i] for i in range(len(answer[2]))):
                part3_passed = False
                print(f"{RED}Part 3 test failed: file={file}, high quality sequences do not match expected output. Solution: {answer[2]}, but got {student[2]}.{RESET}")
                break

    if part3_passed:
        print(f"{GREEN}Part 3 passed :D{RESET}")
    else:
        print(f"{RED}Part 3 failed :({RESET}")


if __name__ == "__main__":
    main()
