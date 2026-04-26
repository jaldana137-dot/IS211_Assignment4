import time
import random

def sequential_search(a_list, item):
    """Searches a list one item at a time from start to end."""
    start = time.time()

    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end = time.time()
    return found, end - start

def ordered_sequential_search(a_list, item):
    """Searches a sorted list one item at a time, stops early if passed the item."""
    start = time.time()

    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end = time.time()
    return found, end - start

def binary_search_iterative(a_list, item):
    """Searches a sorted list by repeatedly splitting it in half (iterative)."""
    start = time.time()

    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time()
    return found, end - start

def binary_search_recursive(a_list, item):
    """Searches a sorted list by repeatedly splitting it in half (recursive)."""
    start = time.time()

    # Call the helper function to do the actual recursion
    result = _binary_search_helper(a_list, item)

    end = time.time()
    return result, end - start

def _binary_search_helper(a_list, item):
    """Helper function for recursive binary search."""
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return _binary_search_helper(a_list[:midpoint], item)
            else:
                return _binary_search_helper(a_list[midpoint + 1:], item)

def main():
    """Runs the benchmark for each search algorithm."""
    sizes = [500, 1000, 5000]
    search_target = 99999999  # this number won't be in our lists

    for size in sizes:
        # Generate 100 random lists of positive integers
        lists = []
        for i in range(100):
            random_list = [random.randint(1, 100000) for _ in range(size)]
            lists.append(random_list)

        # Track total times for each algorithm
        seq_total = 0
        ord_seq_total = 0
        bin_iter_total = 0
        bin_rec_total = 0

        for a_list in lists:
            # Sequential search does not need a sorted list
            _, t = sequential_search(a_list, search_target)
            seq_total += t

            # Sort the list for the remaining searches
            sorted_list = sorted(a_list)

            _, t = ordered_sequential_search(sorted_list, search_target)
            ord_seq_total += t

            _, t = binary_search_iterative(sorted_list, search_target)
            bin_iter_total += t

            _, t = binary_search_recursive(sorted_list, search_target)
            bin_rec_total += t

        # Calculate averages
        seq_avg = seq_total / 100
        ord_seq_avg = ord_seq_total / 100
        bin_iter_avg = bin_iter_total / 100
        bin_rec_avg = bin_rec_total / 100

        # Print results
        print(f"\nFor list size = {size}:")
        print(f"Sequential Search took {seq_avg:10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {ord_seq_avg:10.7f} seconds to run, on average")
        print(f"Binary Search Iterative took {bin_iter_avg:10.7f} seconds to run, on average")
        print(f"Binary Search Recursive took {bin_rec_avg:10.7f} seconds to run, on average")

if __name__ == '__main__':
    main()
