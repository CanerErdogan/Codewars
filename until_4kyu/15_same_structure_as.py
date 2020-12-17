def same_structure_as(original, other):
    if not hasattr(original, '__setitem__') and not hasattr(other, '__setitem__'):
        return True
    elif hasattr(original, '__len__') and hasattr(other, '__len__'):
        if type(original) == type(other) and len(original) == len(other):
            return all(map(lambda pair: same_structure_as(*pair),
                           zip(original, other)))
    return False


assert same_structure_as([1, [1, 1]], [2, [2, 2]]) == True
assert same_structure_as([1, [1, 1]], [[2, 2], 2]) == False
assert same_structure_as([[[], []]], [[[], []]]) == True
assert same_structure_as([[[], []]], [[1, 1]]) == False
assert same_structure_as([], 1) == False
assert same_structure_as([], {}) == False
assert same_structure_as([1, '[', ']'], ['[', ']', 1]) == True
