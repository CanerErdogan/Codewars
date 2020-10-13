def likes(names):
    plural = 's'
    people = names.pop(0) if names else 'no one'
    if names:
        plural = ''
        if len(names) > 1:
            people = ', '.join([people, names.pop(0)])
            if names:
                rest = names.pop(0) if len(names) == 1 else '{} others'.format(len(names))
                people = ' and '.join([people, rest])
        else:
            people = ' and '.join([people, names.pop(0)])

    return '{} like{} this'.format(people, plural)   

print(likes([])) # must be "no one likes this"
print(likes(["Peter"])) # must be "Peter likes this"
print(likes(["Jacob", "Alex"])) # must be "Jacob and Alex like this"
print(likes(["Max", "John", "Mark"])) # must be "Max, John and Mark like this"
print(likes(["Alex", "Jacob", "Mark", "Max"])) # must be "Alex, Jacob and 2 others like this"