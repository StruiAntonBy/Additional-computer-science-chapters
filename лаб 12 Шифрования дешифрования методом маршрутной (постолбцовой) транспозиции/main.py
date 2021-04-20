from functools import reduce


def factorization(num):
    i = 2
    prime_factorization = []
    while num != 1:
        if num % i == 0:
            num = num // i
            prime_factorization.append(i)
            i = 1
        i += 1
    return prime_factorization


def encrypt(text):
    finish_text = reduce(lambda str1, str2: str1 + str2, text.lower().strip().split(' '))

    key = factorization(len(finish_text))

    if len(text) == 1:
        return text

    func = lambda num1, num2: num1 * num2

    a = reduce(func, key[:len(key) // 2], 1)
    b = reduce(func, key[len(key) // 2:], 1)

    matrix = [list(finish_text[i * b: (i + 1) * b]) for i in range(0, a)]

    cipher = ''
    for j in range(0, b):
        for arr in matrix:
            cipher += arr[j]
        if j != b - 1:
            cipher += ' '

    return cipher


def decrypt(cipher):
    if len(cipher) == 1:
        return cipher
    arr_str = cipher.split(' ')
    text = ''
    for i in range(0, len(arr_str[0])):
        for s in arr_str:
            text += s[i]
    return text


c = encrypt(input('Enter the text: '))
print('Encrypted text:', c)
print('Source text:', decrypt(c))
