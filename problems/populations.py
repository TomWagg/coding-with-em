from math import floor


def growth(n_start, fertility, months):
    """Calculate the size of a population after a given number of months.

    Parameters
    ----------
    n_start : int
        The initial population size.
    fertility : int
        The fertility rate (number of offspring per pair).
    months : int
        The number of months to simulate.

    Returns
    -------
    n_total : int
        The total population size after the specified number of months.
    """
    return 0


def time_to_target(n_start, fertility, n_target):
    """Calculate the number of months required for a population to reach a target size.

    Parameters
    ----------
    n_start : int
        The initial population size.
    fertility : int
        The fertility rate (number of offspring per pair).
    n_target : int
        The target population size.

    Returns
    -------
    time : int
        The number of months required to reach the target population size.
    """
    return 0


def time_with_mutation(n_start, fertility, n_target, mutation_factor):
    """Calculate the time for a population to grow to a certain size with mutation after a certain time.

    Parameters
    ----------
    n_start : int
        The initial population size.
    fertility : int
        The fertility rate (number of offspring per pair).
    n_target : int
        The target population size.
    mutation_factor : float
        The factor by which fertility changes after population exceeds 10x initial size. Fertility should
        be multiplied by this factor and floored to the nearest integer.

    Returns
    -------
    time : int
        The number of months required to reach the target population size. If fertility becomes zero
        due to mutation, return -1.
    """
    return 0


def growth_with_capacity(n_start, fertility, months, mutation_factor, island_capacity, n_ferry):
    """Calculate the size of a population over a number of months, considering mutation and
    island capacity constraints.

    Parameters
    ----------
    n_start : int
        The initial population size.
    fertility : int
        The fertility rate (number of offspring per pair).
    months : int
        The number of months to simulate.
    mutation_factor : float
        The factor by which fertility changes after population exceeds 10x initial size. Fertility should
        be multiplied by this factor and floored to the nearest integer.
    island_capacity : int
        The maximum population size the island can support without constraints.
    n_ferry : int
        The number of individuals that can be transported away each month once the ferry is built.

    Returns
    -------
    n_total : int
        The total population size after the specified number of months.
    """
    return 0



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
import populations_solution as sol

# define ansi red and green for terminal output
RED, GREEN, RESET = "\033[91m", "\033[92m", "\033[0m"


def main():
    N_TESTS = 1000

    subsets = [
        ["n_start", "fertility", "months"],
        ["n_start", "fertility", "n_target"],
        ["n_start", "fertility", "n_target", "mutation_factor"],
        ["n_start", "fertility", "months", "mutation_factor", "island_capacity", "n_ferry"]
    ]
    func_names = ["growth", "time_to_target", "time_with_mutation", "growth_with_capacity"]
    answers = [sol.growth, sol.time_to_target, sol.time_with_mutation, sol.growth_with_capacity]
    students = [growth, time_to_target, time_with_mutation, growth_with_capacity]

    for part, arg_subset, f_name, ans_f, stu_f in zip(range(1, 5), subsets, func_names, answers, students):
        part_passed = True
        for _ in range(N_TESTS):
            if not part_passed:
                break
            args = {
                "n_start": random.randint(2, 100),
                "fertility": random.randint(1, 10),
                "months": random.randint(1, 20),
                "n_target": random.randint(1000, 1_000_000),
                "mutation_factor": random.uniform(0.01, 10.0),
                "island_capacity": random.randint(100, 1000),
                "n_ferry": random.randint(10, 100),
            }
            answer = ans_f(**{k: args[k] for k in arg_subset})
            student = stu_f(**{k: args[k] for k in arg_subset})
            if answer != student:
                print(f"  {RED}{f_name}({', '.join([str(args[n]) if isinstance(args[n], int) else f"{args[n]:1.2f}" for n in arg_subset])}) = {student}, expected {answer}{RESET}")
                part_passed = False

        if part_passed:
            print(f"{GREEN}Part {part} passed :){RESET}")
        else:
            print(f"{RED}Part {part} failed :({RESET}")


if __name__ == "__main__":
    main()
