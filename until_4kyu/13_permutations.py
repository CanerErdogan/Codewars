def permutations(string):
    if not string:
        return []
    elif len(string) == 1:
        return string
    else:
        result = set()
        for i in range(len(string)):
            for j in permutations(string[:i] + string[i+1:]):
                result.add(string[i] + j)
        return list(result)


assert sorted(permutations('a')) == ['a']
assert sorted(permutations('ab')) == ['ab', 'ba']
assert sorted(permutations('aabb')) == ['aabb', 'abab', 'abba',
                                        'baab', 'baba', 'bbaa']
assert sorted(permutations('abcd')) == ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb',
                                        'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
                                        'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
                                        'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba']
