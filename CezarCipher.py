def encrypt(key: str, text: str) -> str:
    cipher = ""
    rus = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

    for i in range(0, len(text)):
        if text[i].lower() in rus:
            cipher += rus[(ord(text[i].lower()) + ord(key[i % len(key)].lower()) - 2 * ord('а') + 1) % 33]
        elif text[i] == " ":
            cipher += rus[(32 + ord(key[i % len(key)].lower()) - ord('а') + 1) % 33]
    return cipher


def decrypt(key: str, cipher: str) -> str:
    text = ""
    rus = "абвгдежзийклмнопрстуфхцчшщъыьэюя "

    for i in range(0, len(cipher)):
        if cipher[i].lower() in rus:
            text += rus[(ord(cipher[i].lower()) - ord(key[i % len(key)].lower()) - 1) % 33]
        elif text[i] == " ":
            cipher += rus[(32 - ord(key[i % len(key)].lower()) + ord('а') - 1) % 33]
    return text
