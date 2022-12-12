def encrypt(plainText, key):
    cipherVal = ''
    for i in range(len(plainText)):
        pt = ord(plainText[i]) - 65
        k = ord(key[i % len(key)]) - 65
        c = (pt + k) % 26;

        cipherVal += chr(c + 65)
    return cipherVal


def decrypt(cipher, key):
    plainTextVal = ''
    for i in range(len(cipher)):
        c = ord(cipher[i]) - 65
        k = ord(key[i % len(key)]) - 65
        pt = (c - k) % 26;

        plainTextVal += chr(pt + 65)
    return plainTextVal


def main():
    plainText = 'CRYPTOGRAPHY'
    key = 'ASMT'
    cipher = 'CJKITGSKAHTR'

    eText = encrypt(plainText, key)
    cText = decrypt(cipher, key)

    print(eText)
    print(cText)

main()