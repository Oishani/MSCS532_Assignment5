import random
from deterministic_quicksort import quicksort

def generate_test_cases():
    """
    Generates multiple test cases for quicksort.
    """
    return {
        'empty': [],
        'single_element': [42],
        'sorted': list(range(10)),
        'reverse_sorted': list(range(10, 0, -1)),
        'random_small': random.sample(range(20), 10),
        'random_large': random.sample(range(1000), 100),
        'duplicates': [5, 3, 8, 3, 9, 1, 5, 3],
    }

def run_tests():
    """
    Runs quicksort on all test cases and verifies correctness.
    """
    cases = generate_test_cases()
    for name, arr in cases.items():
        original = arr.copy()
        sorted_arr = quicksort(arr.copy())
        assert sorted_arr == sorted(original), (
            f"Test {name} failed: {sorted_arr} != {sorted(original)}"
        )
        print(f"Test {name} passed. Input: {original}, Output: {sorted_arr}")

if __name__ == '__main__':
    run_tests()
