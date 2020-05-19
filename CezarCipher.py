def encrypt(in_shift: int, text: str) -> str:
    cipher = ""

    for i in text:
        shift = in_shift
        if (ord(i) >= ord('а')) & (ord(i) <= ord('я')):
            shift %= 32
            if ord(i) + shift > ord('я'):
                cipher += (chr(ord(i) + shift - 32))
            else:
                cipher += (chr(ord(i) + shift))
        elif (ord(i) >= ord('А')) & (ord(i) <= ord('Я')):
            shift %= 32
            if ord(i) + shift > ord('Я'):
                cipher += (chr(ord(i) + shift - 32))
            else:
                cipher += (chr(ord(i) + shift))
        elif (ord(i) >= ord('a')) & (ord(i) <= ord('z')):
            shift %= 26
            if ord(i) + shift > ord('z'):
                cipher += (chr(ord(i) + shift - 26))
            else:
                cipher += (chr(ord(i) + shift))
        elif (ord(i) >= ord('A')) & (ord(i) <= ord('Z')):
            shift %= 26
            if ord(i) + shift > ord('Z'):
                cipher += (chr(ord(i) + shift - 26))
            else:
                cipher += (chr(ord(i) + shift))
        else:
            cipher += i

    return cipher


def decrypt(in_shift: int, cipher: str) -> str:
    text = ""

    for i in cipher:
        shift = in_shift
        if (ord(i) >= ord('а')) & (ord(i) <= ord('я')):
            shift %= 32
            if ord(i) - shift < ord('а'):
                text += (chr(ord(i) - shift + 32))
            else:
                text += (chr(ord(i) - shift))
        elif (ord(i) >= ord('А')) & (ord(i) <= ord('Я')):
            shift %= 32
            if ord(i) - shift < ord('А'):
                text += (chr(ord(i) - shift + 32))
            else:
                text += (chr(ord(i) - shift))
        elif (ord(i) >= ord('a')) & (ord(i) <= ord('z')):
            shift %= 26
            if ord(i) - shift < ord('a'):
                text += (chr(ord(i) - shift + 26))
            else:
                text += (chr(ord(i) - shift))
        elif (ord(i) >= ord('A')) & (ord(i) <= ord('Z')):
            shift %= 26
            if ord(i) - shift < ord('A'):
                text += (chr(ord(i) - shift + 26))
            else:
                text += (chr(ord(i) - shift))
        else:
            text += i

    return text
