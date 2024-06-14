def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]
