def quicksort(arr):
    """
    Sorts the list in place using the deterministic Quicksort algorithm.
    Pivot selection: always the first element.
    """
    def _quicksort(items, low, high):
        if low < high:
            # Partition the array and get pivot index
            pivot_index = partition(items, low, high)
            # Recursively sort elements before pivot
            _quicksort(items, low, pivot_index - 1)
            # Recursively sort elements after pivot
            _quicksort(items, pivot_index + 1, high)

    def partition(items, low, high):
        """
        Partition the subarray items[low..high] by selecting the first element as pivot.
        Moves all elements <= pivot to its left and > pivot to its right.
        """
        pivot = items[low]      # deterministic pivot: first element
        left = low + 1
        right = high

        while True:
            # Advance left pointer until finding an element > pivot
            while left <= right and items[left] <= pivot:
                left += 1
            # Move right pointer until finding an element < pivot
            while left <= right and items[right] >= pivot:
                right -= 1
            if left > right:
                break
            # Swap out-of-place elements
            items[left], items[right] = items[right], items[left]

        # Place pivot into its correct position
        items[low], items[right] = items[right], items[low]
        return right

    # Kick off the recursion
    _quicksort(arr, 0, len(arr) - 1)
    return arr
