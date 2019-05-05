#!/usr/bin/env python3

# ./translate_characters.py

# Create a translation dictionary then apply it to a text, character by character.

from string import ascii_lowercase
import clipboard, pyautogui


def functionalize(dictionary, verbose = True):
    def f(x):
        if x in dictionary:
            return dictionary[x]
        else:
            if verbose:
                print(f'Missing key: "{x}".')
            return ''
    return f


def apply_dictionary(dictionary, encrypted_message, verbose):
    return ''.join(map(functionalize(dictionary, verbose), encrypted_message))


def interactively_extend_dictionary(dictionary, encrypted_message):
    '''Warning: dictionary is modified in place.'''

    stop = False
    number_of_additions = 0

    for encrypted_character in encrypted_message:

        if encrypted_character not in dictionary:

            if len(encrypted_character) != 1:
                input(f'Warning: len(encrypted_character) == {len(encrypted_character)} != 1 (value: "{encrypted_character}"). [enter|ctrl-c]')

            clipboard.copy(encrypted_character)
            pyautogui.hotkey('alt', 'tab', interval = pyautogui.PAUSE)
            pyautogui.hotkey('ctrl', 'f', interval = pyautogui.PAUSE)
            pyautogui.hotkey('ctrl', 'v', interval = pyautogui.PAUSE)
            pyautogui.hotkey('alt', 'tab', interval = pyautogui.PAUSE)

            decrypted_character = input(f'decrypted_value for {encrypted_character}: ')

            if decrypted_character == 'STOP':
                stop = True
                break

            if len(decrypted_character) != 1:
                input(f'Warning: len(decrypted_character) == {len(decrypted_character)} != 1 (value: "{decrypted_character}"). [enter|ctrl-c]')

            dictionary[encrypted_character] = decrypted_character
            number_of_additions += 1

    return stop, number_of_additions


def _save(text, filename):
    my_file = open(filename, 'w')
    my_file.write(text)
    my_file.close()


def _read(filename):
    my_file = open(filename, 'r')
    contenu = my_file.read()
    my_file.close()
    return contenu


if __name__ == '__main__':

    # read encrypted message
    encrypted_message = _read(filename = 'translate_characters_data/The_Challenge_of_Fate/encrypted.txt')

    # load dictionary
    from translate_characters_data.The_Challenge_of_Fate.dictionary import dictionary

    # extend dictionary
    stop, number_of_additions = interactively_extend_dictionary(dictionary, encrypted_message)

    if number_of_additions > 0:
        # save dictionary
        _save(
            text = f'dictionary = {dictionary}\n',
            filename = 'translate_characters_data/The_Challenge_of_Fate/dictionary.py'
        )

    # apply dictionary
    decrypted_message = apply_dictionary(dictionary, encrypted_message, verbose = True)

    # print and save decrypted message
    # print(decrypted_message)
    _save(decrypted_message, filename = 'translate_characters_data/The_Challenge_of_Fate/decrypted.txt')
