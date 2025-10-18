import argparse
import random
import matplotlib.pyplot as plt


def genotype_to_phenotype(genotype):
    """Convert a genotype string to a phenotype description."""
    return "A"


def produce_offspring(g1, g2):
    return g1


def next_generation(population, part_four=False, extra_death_rates={}):
    return population


def simulate_generations(initial_population, generations, part_four=False, extra_death_rates={}):
    population = initial_population
    gt_dists = [get_genotype_distribution(population)]
    pt_dists = [get_phenotype_distribution(population)]
    for i in range(generations):
        population = next_generation(population, part_four, extra_death_rates=extra_death_rates)
        gt_dists.append(get_genotype_distribution(population))
        pt_dists.append(get_phenotype_distribution(population))

    return population, gt_dists, pt_dists


def get_genotype_distribution(population):
    genotype_dist = {
        "AA": 0,
        "AO": 0,
        "BB": 0,
        "BO": 0,
        "AB": 0,
        "OO": 0,
    }
    return genotype_dist


def get_phenotype_distribution(population):
    phenotype_dist = {
        "A": 0,
        "B": 0,
        "AB": 0,
        "O": 0,
    }
    return phenotype_dist


#############################################################
#############################################################
########################## STOP! ############################
##### You don't need to change anything below this line #####
#############################################################
#############################################################
#############################################################


def plot_distributions(init_gt_dist, init_pt_dist, final_gt_dist, final_pt_dist):
    # plot a 2x2 grid of bar charts, with the initial and final genotype and phenotype distributions
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    for ax, dist, title in zip(
        axs.flatten(),
        [init_gt_dist, init_pt_dist, final_gt_dist, final_pt_dist],
        [
            "Initial Genotype Distribution",
            "Initial Phenotype Distribution",
            "Final Genotype Distribution",
            "Final Phenotype Distribution",
        ],
    ):
        ax.bar(dist.keys(), dist.values())
        ax.set_title(title)
    plt.tight_layout()
    plt.show()


def plot_type_evolution(gt_dists, pt_dists):
    # side by side line plots showing the evolution of genotype and phenotype fractions over generations
    generations = len(gt_dists)
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    for ax, dists, title in zip(axes, [gt_dists, pt_dists], ["Genotype Evolution", "Phenotype Evolution"]):
        for key in dists[0].keys():
            fractions = [dist[key] / sum(dist.values()) if sum(dist.values()) > 0 else 0 for dist in dists]
            ax.plot(range(generations), fractions, label=key)
        ax.set_title(title)
        ax.set_xlabel("Generation")
        ax.set_ylabel("Fraction of Population")
        ax.legend()

    plt.tight_layout()
    plt.show()


def main(extra_credit=False):
    # Part 1 assessment
    part1_passed = True
    test_cases = {
        "AA": "A",
        "AO": "A",
        "BB": "B",
        "BO": "B",
        "AB": "AB",
        "OO": "O",
    }

    # define ansi red and green for terminal output
    RED, GREEN, RESET = "\033[91m", "\033[92m", "\033[0m"

    for genotype, expected_phenotype in test_cases.items():
        result = genotype_to_phenotype(genotype)
        if result != expected_phenotype:
            part1_passed = False
            print(
                f"{RED}Test failed for genotype {genotype}: expected {expected_phenotype}, got {result}{RESET}"
            )

    if part1_passed:
        print(f"Part 1: {GREEN}PASSED!{RESET}")
    else:
        print(f"Part 1: {RED}FAILED :({RESET}")

    # Part 2 assessment
    part2_passed = True
    test_cases = {
        ("AA", "AO"): ["AA", "AO"],
        ("AB", "BO"): ["AB", "AO", "BB", "BO"],
        ("OO", "OO"): ["OO"],
        ("AB", "AB"): ["AA", "AB", "BB"],
    }
    for (g1, g2), expected_offsprings in test_cases.items():
        result = set()
        for _ in range(100):
            offspring = produce_offspring(g1, g2)
            result.add(offspring)
        if not all(offspring in expected_offsprings for offspring in result) or not all(offspring in result for offspring in expected_offsprings):
            part2_passed = False
            print(
                f"{RED}Test failed for parents {g1} and {g2}: expected {expected_offsprings}, got {result}{RESET}"
            )

    if part2_passed:
        print(f"Part 2: {GREEN}PASSED!{RESET}")
    else:
        print(f"Part 2: {RED}FAILED :({RESET}")

    # Part 3 assessment
    part3_passed = True

    test_cases = [
        (["AA", "AO", "OO"], 3),
        (["AA", "AB", "BO", "OO"], 8),
        (["AA", "BB", "AB", "OO", "BO", "AB", "AO"], 41)
    ]

    for initial_population, expected_count in test_cases:
        unique_populations = set()
        for _ in range(10000):
            new_population = next_generation(initial_population)
            unique_populations.add(tuple(sorted(new_population)))
        if len(unique_populations) != expected_count:
            part3_passed = False
            print(
                f"{RED}Test failed for initial population {initial_population}: expected {expected_count} unique populations, got {len(unique_populations)}{RESET}"
            )

    if part3_passed:
        print(f"Part 3: {GREEN}PASSED!{RESET}")
    else:
        print(f"Part 3: {RED}FAILED :({RESET}")

    # Beyond part 3, it becomes difficult to have deterministic tests due to randomness,
    # especially since people may implement things differently with a different number of random calls,
    # so setting the random seed won't necessarily help. Instead, we'll just run the simulations and print
    # out some results for manual inspection.

    print("It's difficult to have deterministic tests for parts 4 onwards due to randomness. Instead "
          "this code will run some simulations and print out results for manual inspection.")

    print("Part 4: Simulating generations with death rate...")
    initial_population = [("AA", 0), ("AO", 0), ("BB", 0), ("BO", 0), ("AB", 0), ("OO", 0)]
    print(f"  Initial population: {initial_population}")
    print(f"  Population after 2 generations: {simulate_generations(initial_population, 2, part_four=True)}")
    for generations in [5, 10, 15, 20]:
        final_population, gt_dists, pt_dists = simulate_generations(initial_population, generations, part_four=True)
        print(f"  After {generations} generations, population size: {len(final_population)}")

    # if any value in the distributions is greater than 0, plot the distributions
    # if any(value > 0 for value in gt_dists[-1].values()):
    #     plot_distributions(gt_dists[0], pt_dists[0], gt_dists[-1], pt_dists[-1])
    #     plot_phenotype_evolution(pt_dists)

    print("Part 5: Plotting the evolution of blood types over 20 generations...")
    initial_population = [("AA", 0) for _ in range(30)] \
        + [("AO", 0) for _ in range(30)] \
        + [("BB", 0) for _ in range(30)] \
        + [("BO", 0) for _ in range(30)] \
        + [("AB", 0) for _ in range(30)] \
        + [("OO", 0) for _ in range(30)]
    for _ in range(50):
        initial_population.append((random.choice(["AA", "AO", "BB", "BO", "AB", "OO"]), 0))
    final_population, gt_dists, pt_dists = simulate_generations(initial_population, 20,
                                                                part_four=True)

    if any(value > 0 for value in gt_dists[-1].values()): 
        plot_type_evolution(gt_dists, pt_dists)
    else:
        print("  Looks like you haven't done part 5 yet, so no plots to show!")

    if extra_credit:
        print("Extra credit: Changing survival rates...")
        extra_death_rates = {
            "AA": 0.5,
            "AB": 0.5,
            "AO": 0.5
        }
        final_population, gt_dists, pt_dists = simulate_generations(initial_population, 20,
                                                                    part_four=True,
                                                                    extra_death_rates=extra_death_rates)
        if any(value > 0 for value in gt_dists[-1].values()):
            plot_type_evolution(gt_dists, pt_dists, suptitle="Made having AA, AB, AO genotypes more deadly!")
        else:
            print("  Looks like you haven't done the extra credit yet, so no plots to show!")



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Simulate blood type inheritance.")
    parser.add_argument("--extra-credit", "-e", action="store_true", help="Run the extra credit part of the assignment")
    args = parser.parse_args()

    main(args.extra_credit)
