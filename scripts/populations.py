import argparse
from math import floor


def growth(n_start, fertility, months):
    """Calculate the size of a population after a given number of months."""
    # YOUR CODE HERE

    n_total = n_start
    for i in range(months):
        n_new = (n_total // 2) * fertility
        n_total += n_new

    return n_total


def time_to_target(n_start, fertility, n_target):
    """Calculate the number of months required for a population to reach a target size."""

    n_total = n_start
    time = 0
    while n_total < n_target:
        n_new = (n_total // 2) * fertility
        n_total += n_new
        time += 1

    # YOUR CODE HERE
    return time


def time_with_mutation(n_start, fertility, n_target, mutation_factor):
    """Calculate the time for a population to grow with mutation after a certain time."""

    n_total = n_start
    time = 0
    original_fertility = fertility
    while n_total < n_target:
        if n_total >= n_start * 10:
            fertility = floor(original_fertility * mutation_factor)
            if fertility == 0:
                return -1
        n_new = (n_total // 2) * fertility
        n_total += n_new
        time += 1

    # YOUR CODE HERE
    return time


def growth_with_capacity(n_start, fertility, months, mutation_factor, island_capacity, n_ferry):
    """Calculate the time for a population to grow with mutation and island capacity constraints."""
    ferry_built = False
    n_total = n_start
    original_fertility = fertility

    for i in range(months):
        if n_total >= n_start * 10:
            fertility = floor(original_fertility * mutation_factor)
            if fertility == 0:
                return n_total

        print(i, fertility, n_total, ferry_built)

        capacity_exceeded = n_total > island_capacity
        if capacity_exceeded and not ferry_built:
            ferry_built = True

        if capacity_exceeded:
            n_new = (n_total // 2)
        else:
            n_new = (n_total // 2) * fertility
        n_total += n_new


        if ferry_built:
            n_total -= n_ferry
            if n_total < 0:
                n_total = 0

    # YOUR CODE HERE
    return n_total


def main():
    parser = argparse.ArgumentParser(description="Calculate population growth.")
    parser.add_argument("--n_start", "-s", type=int, help="Starting population size")
    parser.add_argument("--fertility", "-f", type=int, help="Fertility rate (offspring per pair of rabbits per month)")
    parser.add_argument("--months", "-m", type=int, help="Number of months to simulate")
    parser.add_argument("--n_target", "-t", type=int, help="Target population size")
    parser.add_argument("--mutation-factor", "-mf", type=float, help="Factor by which fertility changes due to mutation")
    parser.add_argument("--island-capacity", "-c", type=int, help="Maximum population capacity of the island")
    parser.add_argument("--n_ferry", "-d", type=int, help="Number of individuals that can fit on a ferry each month")
    parser.add_argument("--part", "-p", type=int, help="Part of the problem to solve (1-4)")

    args = parser.parse_args()

    if args.part == 1:
        print("Part one:", growth(args.n_start, args.fertility, args.months))
    elif args.part == 2:
        print("Part two:", time_to_target(args.n_start, args.fertility, args.n_target))
    elif args.part == 3:
        print("Part three:", time_with_mutation(args.n_start, args.fertility,
                                                args.n_target, args.mutation_factor))
    elif args.part == 4:
        print("Part four:", growth_with_capacity(args.n_start, args.fertility, args.months,
                                                 args.mutation_factor, args.island_capacity, args.n_ferry))


if __name__ == "__main__":
    main()
