"""
item_counter.py

A simple utility to count occurrences of items in a list.
Demonstrates dictionary usage and counting logic in Python.

Author: [Your Name]
"""

def count_items(item_list):
    """
    Counts the frequency of each item in the list.

    Args:
        item_list (list): List of items.

    Returns:
        dict: Dictionary mapping item -> count.
    """
    counter = {}
    for item in item_list:
        counter[item] = counter.get(item, 0) + 1
    return counter


def main():
    """
    Example usage of the item counter.
    """
    sample_items = ['apple', 'banana', 'orange', 'apple', 'orange', 'apple']
    counts = count_items(sample_items)
    print("Item counts:", counts)


if __name__ == "__main__":
    main()
