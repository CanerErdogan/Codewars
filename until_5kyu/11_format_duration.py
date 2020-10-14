from operator import mul
from functools import reduce


def format_duration(seconds):

    if not seconds:
        return 'now'

    units = {
        'year': 365,
        'day': 24,
        'hour': 60,
        'minute': 60,
        'second': 1
    }

    out = []
    for idx, key in enumerate(units.keys()):
        multiplier = reduce(mul, list(units.values())[idx:])
        amount = seconds // multiplier
        # A better code does not manipulate an input in-place
        seconds -= amount * multiplier
        plural = 's' if amount > 1 else ''
        string = '{} {}{}'.format(amount, key, plural) if amount > 0 else ''
        if string:
            out.append(string)

    return ' and '.join([', '.join(out[:-1]), out[-1]]) if len(out) > 1 else out[0]


assert format_duration(0) == "now"
assert format_duration(1) == "1 second"
assert format_duration(62) == "1 minute and 2 seconds"
assert format_duration(120) == "2 minutes"
assert format_duration(3600) == "1 hour"
assert format_duration(3662) == "1 hour, 1 minute and 2 seconds"
