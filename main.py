from CaesarCoder import caesar_encode, caesar_decode
from VigenereCoder import vigerene_encode, vigerene_decode
from A1Z26Coder import a1z26_encode, a1z26_decode
from AtbashCoder import atbash_code
from MorseCoder import morse_encode, morse_decode

import PySimpleGUI as sg


if __name__ == '__main__':
    def create_main_window():
        sg.theme('DarkGray14')

        layout = [
            [
                sg.Text('PyCoder', key='-LABEL_PYCODER-')
            ],
            [
                sg.Text('Choose your Cipher: ', key='-LABEL_CHOOSE_CIPHER-'),
                sg.Combo(['A1Z26 Cipher', 'Atbash Cipher', 'Caesar Cipher', 'Morse Code', 'Vigenère Cipher'],
                         key='-COMBO_CIPHERS-')
            ],
            [
                sg.Text('Ciphertext Input: ', key='-LABEL_INPUT-'), sg.Multiline(size=(100, 10), key='-PLAINTEXT-')
            ],
            [
                sg.Text('                 Key: '), sg.InputText(key='-KEY-')
            ],
            [
                sg.Text('             Output: '), sg.Output(size=(100, 10), key='-CIPHERTEXT-')
            ],
            [
                sg.Button('Encode', key='-BTN_ENCODE-'), sg.Button('Decode', key='-BTN_DECODE-')
            ]
        ]

        title = 'PyCoder'

        window = sg.Window(title, layout, finalize=True)

        return window


    window = create_main_window()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == '-BTN_ENCODE-':
            if values['-COMBO_CIPHERS-'] == 'A1Z26 Cipher':
                try:
                    print(a1z26_encode(values['-PLAINTEXT-'].upper()))
                except:
                    print('Please, insert valid keys and characters.')
            elif values['-COMBO_CIPHERS-'] == 'Atbash Cipher':
                try:
                    print(atbash_code(values['-PLAINTEXT-'].upper()))
                except:
                    print('Please, insert valid keys and characters.')
            elif values['-COMBO_CIPHERS-'] == 'Caesar Cipher':
                try:
                    print(caesar_encode(int(values['-KEY-']), values['-PLAINTEXT-'].upper()))
                except:
                    print('Please, insert valid keys and characters.')
            elif values['-COMBO_CIPHERS-'] == 'Morse Code':
                try:
                    print(morse_encode(values['-PLAINTEXT-'].upper()))
                except:
                    print('Please, insert valid keys and characters.')
            elif values['-COMBO_CIPHERS-'] == 'Vigenère Cipher':
                try:
                    print(vigerene_encode(values['-KEY-'].upper(), values['-PLAINTEXT-'].upper()))
                except:
                    print('Please, insert valid keys and characters.')
        elif event == '-BTN_DECODE-':
            if values['-COMBO_CIPHERS-'] == 'A1Z26 Cipher':
                try:
                    print(a1z26_decode(values['-PLAINTEXT-']))
                except:
                    print('Please, insert valid keys and characters.')
            elif values['-COMBO_CIPHERS-'] == 'Atbash Cipher':
                try:
                    print(atbash_code(values['-PLAINTEXT-']))
                except:
                    print('Please, insert valid keys and characters.')
            elif values['-COMBO_CIPHERS-'] == 'Caesar Cipher':
               try:
                    print(caesar_decode(int(values['-KEY-']), values['-PLAINTEXT-']))
               except:
                   print('Please, insert valid keys and characters.')
            elif values['-COMBO_CIPHERS-'] == 'Morse Code':
                try:
                    print(morse_decode(values['-PLAINTEXT-']))
                except:
                    print('Please, insert valid keys and characters.')
            elif values['-COMBO_CIPHERS-'] == 'Vigenère Cipher':
                try:
                    print(vigerene_decode(values['-KEY-'], values['-PLAINTEXT-']))
                except:
                    print('Please, insert valid keys and characters.')

    window.close()
