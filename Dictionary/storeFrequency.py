def frequency_dict(lst):
    """
    Create a frequency dictionary from a list of items.

    Args:
        lst (list): A list of items.

    Returns:
        dict: A dictionary with items as keys and their frequencies as values.
    """
    freq_dict = {}
    for item in lst:
        freq_dict[item] = freq_dict.get(item, 0) + 1
    return freq_dict

if __name__ == "__main__":
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(f"Frequency dictionary: {frequency_dict(sample_list)}")