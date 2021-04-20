import config


def encrypt(text, key=config.KEY):
    text = text.upper()
    cipher = ''
    for symbol in text:
        for i, arr in enumerate(config.BASIC_MATRIX):
            try:
                if symbol == 'J':
                    symbol = 'I'
                j = arr.index(symbol)
                cipher += config.NAME_ROW_COLUMN[i] + config.NAME_ROW_COLUMN[j]
            except ValueError:
                continue

    if len(cipher) % len(key) != 0:
        raise ValueError

    matrix = [list(cipher[i * len(key):(i + 1) * len(key)])
              for i in range(0, int(len(cipher) / len(key)))]

    cipher = ''
    list_key = list(key)
    for symbol in sorted(key):
        i = list_key.index(symbol)
        list_key[i] = ' '
        t = ''
        for arr in matrix:
            t += arr[i]
        cipher += t
    return cipher


def decrypt(cipher, key=config.KEY):
    sort_key = list(sorted(key))
    res = list()
    n = int(len(cipher) / len(key))
    for symbol in key:
        i = sort_key.index(symbol)
        sort_key[i] = ' '
        t = list(cipher[i * n: (i + 1) * n])
        res.append(t)

    cipher = ''
    for i in range(0, len(res[0])):
        for arr in res:
            cipher += arr[i]

    text = ''
    for k in range(0, int(len(cipher) / 2)):
        symbol = cipher[k * 2:(k + 1) * 2]
        i = config.NAME_ROW_COLUMN.index(symbol[0])
        j = config.NAME_ROW_COLUMN.index(symbol[1])
        symbol = config.BASIC_MATRIX[i][j]
        if symbol == 'I':
            symbol = '(I or J)'
        text += symbol
    return text


input_data = input('Enter the text: ')
c = None
try:
    c = encrypt(input_data)
except ValueError:
    print('Incorrect text')
    exit()
print('Encrypted text:', c)
print('Decrypted text:', decrypt(c))
