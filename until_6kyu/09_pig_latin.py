def pig_it(text):
    return ' '.join([word[1:] + word[0] + 'ay'
                     if word.isalpha() else word for word in text.split()])
    # piglist = []
    # for word in text.split():
    #     if word.isalpha():
    #         word = word[1:] + word[0] + 'ay'
    #     piglist.append(word)
    # return ' '.join(piglist)


assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
assert pig_it('This is my string') == 'hisTay siay ymay tringsay'
assert pig_it('Pig latin is cool') == "igPay atinlay siay oolcay"
assert pig_it('Hello world !') == "elloHay orldway !"
