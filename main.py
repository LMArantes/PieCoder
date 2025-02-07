from CaesarCoder import caesar_encode, caesar_decode
from VigenereCoder import vigenere_encode, vigenere_decode
from A1Z26Coder import a1z26_encode, a1z26_decode
from AtbashCoder import atbash_code
from MorseCoder import morse_encode, morse_decode


def coder_run():
    while True:

        caesar = False
        vigenere = False
        a1z26 = False
        atbash = False
        morse = False

        cipher_option = input("1. Caesar Cipher\n2. Vigenere Cipher\n3. A1Z26\n4. Atbash Cipher\n5. "
                              "Morse Code\n\nChoose your cipher: ")

        match cipher_option:
            case "1":
                caesar = True
            case "2":
                vigenere = True
            case "3":
                a1z26 = True
            case "4":
                atbash = True
            case "5":
                morse = True
            case _:
                print("Invalid choice.\n")
                continue

        code_option = input("1. Encode\n2. Decode\n\nWould you like to encode or decode? ")

        encode = False
        decode = False

        match code_option:
            case "1":
                encode = True
            case "2":
                decode = True
            case _:
                print("Invalid choice.\n")
                continue

        text = input("Enter the text: ")

        if caesar:
            key = input("Enter the key: ")
            key = int(key)
            if encode:
                cipher_text = caesar_encode(key, text)
                print("Output: ", cipher_text)
            elif decode:
                cipher_text = caesar_decode(key, text)
                print("Output: ", cipher_text)
        elif vigenere:
            key = input("Enter the key: ")
            if encode:
                cipher_text = vigenere_encode(key, text)
                print("Output: ", cipher_text)
            elif decode:
                cipher_text = vigenere_decode(key, text)
                print("Output: ", cipher_text)
        elif a1z26:
            if encode:
                cipher_text = a1z26_encode(text)
                print("Output: ", cipher_text)
            elif decode:
                cipher_text = a1z26_decode(text)
                print("Output: ", cipher_text)
        elif atbash:
            cipher_text = atbash_code(text)
            print("Output: ", cipher_text)
        elif morse:
            if encode:
                cipher_text = morse_encode(text)
                print("Output: ", cipher_text)
            elif decode:
                cipher_text = morse_decode(text)
                print("Output: ", cipher_text)
        break


if __name__ == '__main__':
    coder_run()
