# I do not like how I solved this problem:
#
#   Try-except mechanism is not an elegant solution for detection,
#   If-condition is too long.


from itertools import cycle


def snail(snail_map):
    vectors = cycle([(1, 0), (0, 1), (-1, 0), (0, -1)])
    x, y = 0, 0
    try:
        result = [snail_map[y][x]]
    except:
        return []
    visited = [(x, y)]
    dx, dy = next(vectors)
    while len(result) < len(snail_map) * len(snail_map[0]):
        if (x + dx, y + dy) not in visited and 0 <= x + dx < len(snail_map[0]) and 0 <= y + dy < len(snail_map):
            x, y = x + dx, y + dy
            result.append(snail_map[y][x])
            visited.append((x, y))
        else:
            dx, dy = next(vectors)

    return result


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert snail(array) == expected


array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert snail(array) == expected

assert snail([]) == []
assert snail([[]]) == []
