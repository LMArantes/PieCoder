alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


def a1z26_encode(plaintext):
    ciphertext_list = []

    for i in plaintext:
        if i in alphabet:
            ciphertext_list.append(str(alphabet.index(i)+1))

    ciphertext_str = ' '.join(ciphertext_list)
    return ciphertext_str


def a1z26_decode(ciphertext):
    plaintext_list = []
    ciphertext_list = ciphertext.split(' ')

    for i in ciphertext_list:
        plaintext_list.append(alphabet[int(i)-1])

    plaintext_str = ''.join(plaintext_list)

    return plaintext_str
