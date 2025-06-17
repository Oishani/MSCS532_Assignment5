import random

def randomized_quicksort(arr):
    """
    Sorts the list in place using the randomized Quicksort algorithm.
    Pivot selection: randomly chosen from the current subarray.
    """
    def _quicksort(items, low, high):
        if low < high:
            # Randomly select pivot index and move it to the start
            pivot_index = random.randint(low, high)
            items[low], items[pivot_index] = items[pivot_index], items[low]
            # Partition and get final pivot position
            partition_index = partition(items, low, high)
            # Recursively sort elements before and after pivot
            _quicksort(items, low, partition_index - 1)
            _quicksort(items, partition_index + 1, high)

    def partition(items, low, high):
        """
        Partition the subarray using the element at 'low' as the pivot.
        """
        pivot = items[low]
        left = low + 1
        right = high

        while True:
            while left <= right and items[left] <= pivot:
                left += 1
            while left <= right and items[right] >= pivot:
                right -= 1
            if left > right:
                break
            items[left], items[right] = items[right], items[left]

        items[low], items[right] = items[right], items[low]
        return right

    _quicksort(arr, 0, len(arr) - 1)
    return arr
