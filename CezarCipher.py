def encrypt(key: str, text: str) -> str:
    cipher = ""

    for i in range(0, len(text)):
        if(text[i] >= 'а') & (text[i] <= 'я'):
            cipher += chr((ord(text[i]) + ord(key[i % len(key)]) - 2 * ord('а') + 1) % 32 + ord('а'))
        elif (text[i] >= 'А') & (text[i] <= 'Я'):
            cipher += chr((ord(text[i]) + ord(key[i % len(key)]) - 2 * ord('А') + 1) % 32 + ord('А'))
        elif (text[i] >= 'a') & (text[i] <= 'z'):
            cipher += chr((ord(text[i]) + ord(key[i % len(key)]) - 2 * ord('a') + 1) % 26 + ord('a'))
        elif (text[i] >= 'A') & (text[i] <= 'Z'):
            cipher += chr((ord(text[i]) + ord(key[i % len(key)]) - 2 * ord('A') + 1) % 26 + ord('A'))
        else:
            cipher += text[i]
    return cipher


def decrypt(key: str, cipher: str) -> str:
    text = ""

    for i in range(0, len(cipher)):
        if (cipher[i] >= 'а') & (cipher[i] <= 'я'):
            text += chr((ord(cipher[i]) - ord(key[i % len(key)]) - 2 * ord('а') - 1) % 32 + ord('а'))
        elif (cipher[i] >= 'А') & (cipher[i] <= 'Я'):
            text += chr((ord(cipher[i]) - ord(key[i % len(key)]) - 2 * ord('А') - 1) % 32 + ord('А'))
        elif (cipher[i] >= 'a') & (cipher[i] <= 'z'):
            text += chr((ord(cipher[i]) - ord(key[i % len(key)]) - 2 * ord('a') - 1) % 26 + ord('a'))
        elif (cipher[i] >= 'A') & (cipher[i] <= 'Z'):
            text += chr((ord(cipher[i]) - ord(key[i % len(key)]) - 2 * ord('A') - 1) % 26 + ord('A'))
        else:
            text += cipher[i]
    return text
