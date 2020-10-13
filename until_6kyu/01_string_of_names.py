def namelist(names):
    if names:
        comma_list = list(map(lambda x: x['name'], names[:-1]))
        comma_string = ', '.join(comma_list)
        # return ' & '.join([comma_string, names[-1]['name']]) if comma_string else names[-1]['name']
        return '{} & {}'.format(comma_string, names[-1]['name']) if comma_string else names[-1]['name']
    else:
        return ''


print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
print(namelist([{'name': 'Bart'}]))
print(namelist([]))
