alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


def atbash_code(plaintext):
    ciphertext_list = []

    for i in plaintext:
        if i in alphabet:
            j = alphabet.index(i)
            ciphertext_list.append(alphabet[(j+1)*-1])
        else:
            ciphertext_list.append(i)

    ciphertext_str = ''.join(ciphertext_list)
    return ciphertext_str
