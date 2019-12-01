vowels = ['a', 'e', 'i', 'o', 'u']


def find(word):
    '''
    Finding m
    '''
    groups = 0
    flag = 1
    #flag is 1 until a vowel is found
    vowel_found = 0
    for index, letter in enumerate(word):
        if letter in vowels:
            flag = 0
            vowel_found = 1
        elif index != 0 and letter is 'y' and word[index-1] not in vowels:
            flag = 0
            vowel_found = 1
        elif not flag:
            if vowel_found:
                groups += 1
                vowel_found = 0
    return groups


def double_letters(word):
    '''
    *d
    '''
    if len(word) >= 2:
        if word[-1] == word[-2]:
            return True
    return False


def vowel_before_suffix(word, suffix):
    word = word[:-len(suffix)]    
    for letter in word:
        if letter in vowels:
            return True
    return False


def cvc(word):
    # *o here * is 0 or more due to fil(ing) case
    bad_letters = ['w', 'x', 'y']
    if len(word) >= 3:
        if word[-1] in bad_letters:
            return False
        elif word[-1] not in vowels and word[-2] in vowels and word[-3] not in vowels:
            return True
    return False


def step1a(word):
    suffixes = ['sses', 'ies', 'ss', 's']
    nsuffixes = ['ss', 'i', 'ss', '']
    for index, suffix in enumerate(suffixes):
        if word.endswith(suffix):
            return word[:-len(suffix)] + nsuffixes[index]
    return word


def step1b1(word):
    bad_letters = ['l', 's', 'z']
    suffixes = ['at', 'bl', 'iz']
    nsuffixes = ['ate', 'ble', 'ize']
    for index, suffix in enumerate(suffixes):
        if word.endswith(suffix):
            return word[:-len(suffix)] + nsuffixes[index]
    if double_letters(word) and word[-1] not in bad_letters:
        return word[:-1]
    elif find(word) == 1 and cvc(word):
        return word + 'e'
    return word


def step1b(word):
    if word.endswith('eed'):
        if find(word[:-len('eed')]) > 0:
            return word[:-len('eed')] + 'ee'
        else:
            return word
    if word.endswith('ed'):                
        if vowel_before_suffix(word, 'ed'):
            return step1b1(word[:-len('ed')])
        else:
            return word    
    if word.endswith('ing'):
        if vowel_before_suffix(word, 'ing'):
            return step1b1(word[:-len('ing')])
        else:
            return word            
    return word


def step1c(word):
    if word.endswith('y'):
        if vowel_before_suffix(word, 'y'):
            return word[:-1] + 'i'
            
    return word


def step2(word):
    suffixes = ['ational', 'tional', 'enci', 'anci', 'izer', 'abli', 'alli', 'entli', 'eli', 'ousli',
                'ization', 'ation', 'ator', 'alism', 'iveness', 'fulness', 'ousness', 'aliti', 'iviti', 'biliti']
    nsuffixes = ['ate', 'tion', 'ence', 'ance', 'ize', 'able', 'al', 'ent', 'e', 'ous', 'ize', 'ate', 'ate', 'al',
                 'ive', 'ful', 'ous', 'al', 'ive', 'ble']
    for index, suffix in enumerate(suffixes):
        if word.endswith(suffix):
            if find(word[:-len(suffix)]) > 0:
                return word[:-len(suffix)] + nsuffixes[index]
    return word


def step3(word):
    suffixes = ['icate', 'ative', 'alize', 'iciti', 'ical', 'ful', 'ness']
    nsuffixes = ['ic', '', 'al', 'ic', 'ic', '', '']
    for index, suffix in enumerate(suffixes):
        if word.endswith(suffix):
            if find(word[:-len(suffix)]) > 0:
                return word[:-len(suffix)] + nsuffixes[index]
    return word


def step4(word):
    suffixes = ['al', 'ance', 'ence', 'er', 'ic', 'able', 'ible', 'ant', 'ement', 'ment', 'ent', 'ou',
                'ism', 'ate', 'iti', 'ous', 'ive', 'ize']
    for index, suffix in enumerate(suffixes):
        if word.endswith(suffix):
            if find(word[:-len(suffix)]) > 1:
                return word[:-len(suffix)]

            else:
                return word   
    if word.endswith('ion'):
            temp_word = word[:-len('ion')]
            if find(word[:-len('ion')]) > 1 and temp_word[-1] == 's' or temp_word[-1] == 't':
                return word[:-len('ion')]
    return word


def step5a(word):
    if word.endswith('e'):
        if find(word[:-len('e')]) > 1:
            return word[:-len('e')]
        elif find(word[:-len('e')]) == 1 and cvc(word[:-len('e')]) is False:
            print('afas')
            return word[:-len('e')]
    return word


def step5b(word):
    if find(word) > 1 and double_letters(word) and word.endswith('l'):
        return word[:-1]
    return word


def process(word):
    word = step1a(word)
    # print(word)
    word = step1b(word)
    # print(word)
    word = step1c(word)
    # print(word)
    word = step2(word)
    # print(word)
    word = step3(word)
    # print(word)
    word = step4(word)    
    # print(word)
    word = step5a(word)
    # print(word)
    word = step5b(word)
    # print(word)
    return word

def input_for_stemmer():
    sent = str(input())
    sent = sent.lower()
    sent = sent.split(' ')
    stemmed = []
    for word in sent:                
        if len(word) > 2:
            # for words like 'is' .etc
            stemmed.append(process(word))
        else:            
            stemmed.append(word)
    return ' '.join(stemmed)        

if __name__ == "__main__":
    print(input_for_stemmer())          
