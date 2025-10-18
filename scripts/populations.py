import argparse
from math import floor


def growth(n_start, fertility, months):
    """Calculate the size of a population after a given number of months."""
    # YOUR CODE HERE
    return 0


def time_to_target(n_start, fertility, n_target):
    """Calculate the number of months required for a population to reach a target size."""
    # YOUR CODE HERE
    return 0


def time_with_mutation(n_start, fertility, n_target, mutation_factor):
    """Calculate the time for a population to grow with mutation after a certain time."""
    # YOUR CODE HERE
    return 0


def growth_with_capacity(n_start, fertility, months, mutation_factor, island_capacity, n_ferry):
    """Calculate the time for a population to grow with mutation and island capacity constraints."""
    # YOUR CODE HERE
    return 0


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
