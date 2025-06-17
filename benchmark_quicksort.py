import time
import random
import matplotlib.pyplot as plt
import sys
from deterministic_quicksort import quicksort
from randomized_quicksort import randomized_quicksort

# Raise the recursion limit to support deeper call stacks
sys.setrecursionlimit(10000)

def generate_inputs(sizes, distribution):
    datasets = []
    for size in sizes:
        if distribution == "random":
            data = random.sample(range(size * 10), size)
        elif distribution == "sorted":
            data = list(range(size))
        elif distribution == "reverse":
            data = list(range(size, 0, -1))
        else:
            raise ValueError("Unknown distribution")
        datasets.append((size, data))
    return datasets

def measure_time(sort_fn, data):
    try:
        start = time.perf_counter()
        sort_fn(data.copy())
        end = time.perf_counter()
        return end - start
    except RecursionError:
        print(f"RecursionError for input size {len(data)} with {sort_fn.__name__}")
        return None

def run_benchmarks():
    sizes = [100, 500, 1000, 5000, 10000]
    distributions = ["random", "sorted", "reverse"]
    results = { "deterministic": {}, "randomized": {} }

    for dist in distributions:
        results["deterministic"][dist] = []
        results["randomized"][dist] = []
        datasets = generate_inputs(sizes, dist)
        for size, data in datasets:
            print(f"Running benchmark for size {size} ({dist})...")
            t_det = measure_time(quicksort, data)
            t_rand = measure_time(randomized_quicksort, data)
            results["deterministic"][dist].append((size, t_det))
            results["randomized"][dist].append((size, t_rand))

    # Plotting
    for dist in distributions:
        plt.figure()
        det_data = [(s, t) for s, t in results["deterministic"][dist] if t is not None]
        rand_data = [(s, t) for s, t in results["randomized"][dist] if t is not None]

        if det_data:
            sizes_det, times_det = zip(*det_data)
            plt.plot(sizes_det, times_det, label="Deterministic")

        if rand_data:
            sizes_rand, times_rand = zip(*rand_data)
            plt.plot(sizes_rand, times_rand, label="Randomized")

        plt.title(f"Quicksort Benchmark - {dist.capitalize()} Input")
        plt.xlabel("Input Size")
        plt.ylabel("Time (seconds)")
        plt.legend()
        plt.grid(True)
        plt.savefig(f"quicksort_{dist}_benchmark.png")

    print("Benchmarking complete. Plots saved.")

if __name__ == "__main__":
    run_benchmarks()
