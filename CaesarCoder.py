alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


def caesar_encode(key, plaintext):
    ciphertext_list = []

    for i in plaintext:
        if i in alphabet:
            n = alphabet.index(i)
            lever = n + key
            if lever >= 26:
                lever -= 26
            ciphertext_list.append(alphabet[lever])
        else:
            ciphertext_list.append(i)

    ciphertext_str = ''.join(ciphertext_list)
    return ciphertext_str


def caesar_decode(key, ciphertext):
    plaintext_list = []

    for i in ciphertext:
        if i in alphabet:
            n = alphabet.index(i)
            plaintext_list.append(alphabet[n-key])
        else:
            plaintext_list.append(i)

    plaintext_str = ''.join(plaintext_list)
    return plaintext_str
