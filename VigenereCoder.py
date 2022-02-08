alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


def vigerene_encode(key, plaintext):
    plaintext_length = len(plaintext)
    full_length_keyword_list = []
    ciphertext_list = []

    for i in range(plaintext_length):
        if i+1 > (len(key)):
            j = i//len(key)
            i -= j*len(key)
        full_length_keyword_list.append(key[i])

    for i in range(plaintext_length):
        lever = alphabet.index(full_length_keyword_list[i])
        lever = alphabet.index(plaintext[i]) + lever
        if lever >= 26:
            lever -= lever//26*26

        new_char = alphabet[lever]
        ciphertext_list.append(new_char)

    ciphertext_str = ''.join(ciphertext_list)

    return ciphertext_str


def vigerene_decode(key, ciphertext):
    ciphertext_length = len(ciphertext)
    full_length_keyword_list = []
    plaintext_list = []

    for i in range(ciphertext_length):
        if i+1 > (len(key)):
            j = i//len(key)
            i -= j*len(key)
        full_length_keyword_list.append(key[i])

    for i in range(ciphertext_length):
        lever = alphabet.index(ciphertext[i]) - alphabet.index(full_length_keyword_list[i])
        new_char = alphabet[lever]
        plaintext_list.append(new_char)

    plaintext_str = ''.join(plaintext_list)

    return plaintext_str
