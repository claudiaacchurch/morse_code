morse_dict = {'a': ".-", "b": "-...", 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
              'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
              'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
              's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
              'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '....-', '6': '-....', '7': '--...', '8': '---..',
              '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
              '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'}


def encode(encode_text):
    end_text = ''
    for char in encode_text:
        if char in morse_dict:
            end_text += f"{morse_dict[char] } "
        else:
            print("Invalid symbol(s), please try again.")
    print(end_text)


def decode(decode_text):
    end_text = ''
    cipher_text = decode_text.split(" ")
    try:
        for char in cipher_text:
            key_list = list(morse_dict.keys())
            val_list = list(morse_dict.values())
            position = val_list.index(char)
            new_char = key_list[position]
            end_text += new_char
    except ValueError:
        print('Invalid code, please try again.')

    print(end_text)


should_continue = True
while True:
    encode_or_decode = input("Do you want to 'encode'(into morse) or 'decode'(out of morse)? ").lower()
    if encode_or_decode == "encode":
        phrase_to_encode = input("What would you like to convert into morse code? ").lower()
        encode(encode_text=phrase_to_encode)
    elif encode_or_decode == 'decode':
        phrase_to_decode = input("What would you like to decode from morse code (only use ['.', '-', '/', ' '] ? ").lower()
        decode(decode_text=phrase_to_decode)
    else:
        print("Please enter either 'encode' or 'decode' ")

    another_turn = input("Do you want to do another translation: yes or no? ").lower()
    if another_turn == 'no':
        should_continue = False
        break


