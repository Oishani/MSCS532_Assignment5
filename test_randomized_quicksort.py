import random
from randomized_quicksort import randomized_quicksort

def generate_test_cases():
    """
    Generates diverse test arrays for verifying randomized Quicksort.
    """
    return {
        'empty': [],
        'single_element': [99],
        'sorted': list(range(15)),
        'reverse_sorted': list(range(20, 0, -1)),
        'random_small': random.sample(range(50), 10),
        'random_large': random.sample(range(1000), 100),
        'duplicates': [4, 7, 2, 7, 4, 2, 2, 7],
    }

def run_tests():
    """
    Runs randomized_quicksort on all test cases and checks correctness.
    """
    cases = generate_test_cases()
    for name, arr in cases.items():
        original = arr.copy()
        sorted_arr = randomized_quicksort(arr.copy())
        assert sorted_arr == sorted(original), (
            f"Test {name} failed: {sorted_arr} != {sorted(original)}"
        )
        print(f"Test {name} passed. Input: {original}, Output: {sorted_arr}")

if __name__ == '__main__':
    run_tests()
