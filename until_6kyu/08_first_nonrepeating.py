def first_non_repeating_letter(string):
    for char in string.lower():
        if string.lower().count(char) == 1:
            return string[string.lower().find(char)]
    return ''

assert first_non_repeating_letter('a') == 'a'
assert first_non_repeating_letter('stress') == 't'
assert first_non_repeating_letter('moonmen') == 'e'
assert first_non_repeating_letter('') == ''
assert first_non_repeating_letter('abba') == ''
assert first_non_repeating_letter('aa') == ''
assert first_non_repeating_letter('~><#~><') == '#'
assert first_non_repeating_letter('hello world == eh?') == 'w'
assert first_non_repeating_letter('sTreSS') == 'T'
assert first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!') == ','