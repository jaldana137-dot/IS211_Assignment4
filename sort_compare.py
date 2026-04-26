import time
import random

def insertion_sort(a_list):
    """Sorts a list using the insertion sort algorithm."""
    start = time.time()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    end = time.time()
    return end - start

def shell_sort(a_list):
    """Sorts a list using the shell sort algorithm."""
    start = time.time()

    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2

    end = time.time()
    return end - start

def gap_insertion_sort(a_list, start, gap):
    """Helper function for shell sort - does a gapped insertion sort."""
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

def python_sort(a_list):
    """Sorts a list using Python's built-in sort function."""
    start = time.time()
    a_list.sort()
    end = time.time()
    return end - start

def main():
    """Runs the benchmark for each sorting algorithm."""
    sizes = [500, 1000, 5000]

    for size in sizes:
        # Track total times for each algorithm
        insert_total = 0
        shell_total = 0
        python_total = 0

        for i in range(100):
            # Generate a random list of positive integers
            random_list = [random.randint(1, 100000) for _ in range(size)]

            # Make copies so each algorithm sorts the same unsorted list
            list_for_insert = list(random_list)
            list_for_shell = list(random_list)
            list_for_python = list(random_list)

            # Time each sort
            insert_total += insertion_sort(list_for_insert)
            shell_total += shell_sort(list_for_shell)
            python_total += python_sort(list_for_python)

        # Calculate averages
        insert_avg = insert_total / 100
        shell_avg = shell_total / 100
        python_avg = python_total / 100

        # Print results
        print(f"\nFor list size = {size}:")
        print(f"Insertion Sort took {insert_avg:10.7f} seconds to run, on average")
        print(f"Shell Sort took {shell_avg:10.7f} seconds to run, on average")
        print(f"Python Sort took {python_avg:10.7f} seconds to run, on average")

if __name__ == '__main__':
    main()
