def ascii_generator(text):
    ascii_set = []
    for char in text:
        ascii_set.append(ord(char))

    return ascii_set


def inverseModulo(target, modulo_num, key):
    pengali = 1
    test = -1
    while test < 0:
        test = modulo_num * pengali + target - key
        pengali += 1

    return test


def splitToNBlock(target_list, block_size):
      
    nBlockList = []
    
    for index in range(len(target_list)):
        if(index % block_size == 0):
            if index != 0:
                nBlockList.append(block)
            block = []
        block.append(target_list[index])
        if index == len(target_list) - 1:
                nBlockList.append(block)

    return nBlockList


def reverseNBlockList(target_list):
    return target_list[::-1]


def joinBlockedList(target_list):
    joinedList = []

    for block in target_list:
        for char in block:
            joinedList.append(char)

    return joinedList


def getBlockSize(plain_text):
    for i in range(len(plain_text)):
        if i != 0 and i != 1:
            if len(plain_text) % i == 0:
                return i


def sequenceReverseProcessing(target_list, block_size):
    return joinBlockedList(reverseNBlockList(splitToNBlock(target_list, block_size)))


def listToString(target_list, conv_from_ascii):
    new_string = ""

    for char in target_list:
        if conv_from_ascii:
            new_string += chr(char)  
        else:  
            new_string += char

    return new_string


def key_generator(plain_text, triggering_word):
    # generate ascii code from triggering word''
    triggering_word_ascii = ascii_generator(triggering_word)
    
    key_1 = []

    for index in range(len(plain_text)):
        key_1.append(triggering_word_ascii[index % len(triggering_word_ascii)])

    key_2 = len(triggering_word_ascii)

    block_size = getBlockSize(plain_text)
    
    key_3 = sequenceReverseProcessing(key_1, block_size)

    super_key = []
    for key_index in range(len(key_1)):
        if (key_index % 2 == 0):
            super_key.append((key_1[key_index] + key_2) * key_3[key_index])
        else:
            super_key.append((key_1[key_index] - key_2) * key_3[key_index])
        

    return super_key


def readFile(file):
    text = ""
    with open(file, 'r') as file:
        for line in file:
            text += line
    return text


def writeFile(file_name, content, msg):
    with open(file_name, 'w') as file:
        file.write(content)
    
    print()
    print(msg)




def encryptingText(plain_text, triggering_word):
    super_key = key_generator(plain_text, triggering_word)
    plain_text_ascii = ascii_generator(plain_text)

    cipher_list_unreversed = []

    for index in range(len(plain_text_ascii)):
        plain_char = plain_text_ascii[index]
        current_key = super_key[index]

        cipher_char = (plain_char + current_key) % 255
        cipher_list_unreversed.append(cipher_char)

    cipher_list_reversed = sequenceReverseProcessing(cipher_list_unreversed, getBlockSize(plain_text))
    cipher_text_final = listToString(cipher_list_reversed, True)

    return cipher_text_final
    


def decryptingText(cipher_text, triggering_word):
    super_key = key_generator(cipher_text, triggering_word)
    cipher_text_ascii = ascii_generator(cipher_text)

    cipher_text_ascii_reversed = sequenceReverseProcessing(cipher_text_ascii, getBlockSize(cipher_text))

    plain_list = []

    for index in range(len(cipher_text_ascii_reversed)):
        cipher_char = cipher_text_ascii_reversed[index]
        current_key = super_key[index]

        plain_char = inverseModulo(cipher_char, 255, current_key)
        plain_list.append(chr(plain_char))

    return listToString(plain_list, False)


def encryptingFile(file, triggering_word):
    plain_text = readFile(file)

    super_key = key_generator(plain_text, triggering_word)
    plain_text_ascii = ascii_generator(plain_text)

    cipher_list_unreversed = []

    for index in range(len(plain_text_ascii)):
        plain_char = plain_text_ascii[index]
        current_key = super_key[index]

        cipher_char = (plain_char + current_key) % 255
        cipher_list_unreversed.append(cipher_char)

    cipher_list_reversed = sequenceReverseProcessing(cipher_list_unreversed, getBlockSize(plain_text))
    cipher_text_final = listToString(cipher_list_reversed, True)

    writeFile('cipher_text.txt', cipher_text_final, 'Success Generating Cipher File !')


def decryptingFile(file, triggering_word):
    cipher_text = readFile(file)

    super_key = key_generator(cipher_text, triggering_word)
    cipher_text_ascii = ascii_generator(cipher_text)

    cipher_text_ascii_reversed = sequenceReverseProcessing(cipher_text_ascii, getBlockSize(cipher_text))

    plain_list = []

    for index in range(len(cipher_text_ascii_reversed)):
        cipher_char = cipher_text_ascii_reversed[index]
        current_key = super_key[index]

        plain_char = inverseModulo(cipher_char, 255, current_key)
        plain_list.append(chr(plain_char))

    writeFile('decrypted_cipher_text.txt', listToString(plain_list, False), 'Success Generating Plain File !')

