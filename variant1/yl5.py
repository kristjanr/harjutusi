def liblikas(string):
    try:
        words = string.split()
    except AttributeError:
        return None
    have_replaced = False
    new_sentence = []
    for word in reversed(words):
        if not have_replaced and word[0].lower() == 'a':
            new_sentence.append('liblikas')
            have_replaced = True
            continue
        new_sentence.append(word)
    return ' '.join(reversed(new_sentence))
