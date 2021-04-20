import config


def encrypt(text, key=config.KEY, abc=config.BASIC_ABC):
    cipher = ''
    for x in text:
        elem_isupper = True if x.isupper() else False
        elem = x.upper()
        if elem in abc:
            index = abc.index(elem)
            if index + key >= len(abc):
                if elem_isupper:
                    cipher += abc[abs(len(abc) - (index + key))]
                else:
                    cipher += abc[abs(len(abc) - (index + key))].lower()
            else:
                if elem_isupper:
                    cipher += abc[index + key]
                else:
                    cipher += abc[index + key].lower()
        else:
            cipher += x
    return cipher


def decrypt(cipher, key=config.KEY, abc=config.BASIC_ABC):
    text = ''
    for x in cipher:
        elem_isupper = True if x.isupper() else False
        elem = x.upper()
        if elem in abc:
            index = abc.index(elem)
            if index - key < 0:
                if elem_isupper:
                    text += abc[abs(len(abc) + (index - key))]
                else:
                    text += abc[abs(len(abc) + (index - key))].lower()
            elif index - key >= len(abc):
                if elem_isupper:
                    text += abc[abs(len(abc) - (index - key))]
                else:
                    text += abc[abs(len(abc) - (index - key))].lower()
            else:
                if elem_isupper:
                    text += abc[index - key]
                else:
                    text += abc[index - key].lower()
        else:
            text += x
    return text


print('Key:', config.KEY)
h = encrypt(input('Enter the text: '))
print('Caesar\'s cipher:', h)
print('Source text:', decrypt(h))
