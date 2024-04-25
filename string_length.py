def calculate_length(x):
    if x is None:
        return "Input cannot be None"
    elif not isinstance(x, str):
        return "Input must be a string"
    else:
        return len(x)


print(calculate_length(112))

