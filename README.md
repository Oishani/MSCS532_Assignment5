# MSCS532 Assignment 5: Quicksort Algorithm – Implementation, Analysis, and Randomization

### Oishani Ganguly

This repository contains all Python source code, benchmarks, test results, and analysis for randomized and dewterministic implementations of the Quicksort algorithm.

## Repository Structure

```graphql
├── benchmark_quicksort.py               # Benchmarking script to compare performance
├── deterministic_quicksort.py           # Deterministic Quicksort (first-element pivot)
├── randomized_quicksort.py              # Randomized Quicksort (random pivot)
├── test_deterministic_quicksort.py      # Unit tests for deterministic version
├── test_randomized_quicksort.py         # Unit tests for randomized version
├── results_deterministic_quicksort.txt  # Test output for deterministic version
├── results_randomized_quicksort.txt     # Test output for randomized version
├── quicksort_random_benchmark.png       # Runtime plot on random inputs
├── quicksort_sorted_benchmark.png       # Runtime plot on sorted inputs
├── quicksort_reverse_benchmark.png      # Runtime plot on reverse-sorted inputs
├── MSCS-532_Assignment_5_Quicksort_Algorithm_Implementation_Analysis_and_Randomization.pdf
│                                        # Final written report
└── README.md                            # This file
```

## How to Run

### Install Requirements
```bash
pip3 install matplotlib
```

### Run Tests
```bash
python3 test_deterministic_quicksort.py > results_deterministic_quicksort.txt
python3 test_randomized_quicksort.py > results_randomized_quicksort.txt
```

### Run Benchmarks
```bash
python3 benchmark_quicksort.py
```

This will generate three plots comparing the two algorithms on different types of input distributions.

## Summary

- **Deterministic Quicksort:** Uses the first element as pivot. Simple but can degrade to O(n²) on sorted/reverse inputs.
- **Randomized Quicksort:** Uses a randomly selected pivot to reduce the chance of worst-case partitions, ensuring robust O(n log n) average performance.
- **Empirical Results:** Benchmarks confirm that randomized Quicksort is more consistent across all input types, while the deterministic version fails dramatically on ordered data.

## Results

See the PNG files for visual comparisons:
- `quicksort_random_benchmark.png`
- `quicksort_sorted_benchmark.png`
- `quicksort_reverse_benchmark.png`

## Report

The report `MSCS-532_ Assignment 5_ Quicksort Algorithm_ Implementation, Analysis, and Randomization.pdf` presents the implementation discussion and analysis of the deterministic and randomized Quicksort algorithms, highlighting how randomization improves performance consistency across varied input distributions.