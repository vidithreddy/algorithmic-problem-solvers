"""
string_parser.py

A simple utility to parse a text input, tokenize it, and perform basic transformations.
Demonstrates string manipulation and parsing skills in Python.

Author: [Your Name]
"""

def parse_and_transform(input_string):
    """
    Parses a comma-separated input string and transforms it into a list of stripped items.

    Args:
        input_string (str): Raw input string with comma-separated values.

    Returns:
        list: Cleaned list of items.
    """
    tokens = input_string.strip().split(',')
    cleaned_tokens = [token.strip() for token in tokens if token.strip()]
    return cleaned_tokens


def main():
    """
    Example usage of the string parser.
    """
    sample_input = "apple, banana , orange ,grape,,"
    parsed = parse_and_transform(sample_input)
    print("Parsed items:", parsed)


if __name__ == "__main__":
    main()
