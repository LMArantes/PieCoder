morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': '/',
    '1': '·----',
    '2': '··---',
    '3': '···--',
    '4': '····-',
    '5': '·····',
    '6': '-····',
    '7': '--···',
    '8': '---··',
    '9': '----·',
    '0': '-----',
}


def morse_encode(plaintext):
    ciphertext_list = []

    for i in plaintext:
        ciphertext_list.append(morse.get(i))

    ciphertext_str = ' '.join(ciphertext_list)
    return ciphertext_str


def morse_decode(ciphertext_str):
    plaintext_list = []
    ciphertext_list = ciphertext_str.split(' ')

    for i in ciphertext_list:
        j = list(morse.values())
        k = list(morse.keys())
        plaintext_list.append(k[j.index(i)])

    plaintext_str = ''.join(plaintext_list)
    return plaintext_str
