def encrypt(plainText, shift):
    text = ''
    for i in range(len(plainText)):
        el = ((ord(plainText[i]) - 65) + shift) % 26
        text += chr(el + 65)
    return text

def decrypt(cipherText, shift):
    text = ''
    for i in range(len(cipherText)):
        el = ((ord(cipherText[i]) - 65) - shift) % 26
        text += chr(el + 65)
    return text

def main():
    plainText = 'ZBC'
    shift = -2

    cipherText = encrypt(plainText, shift)
    print("\nEncryption") 
    print("Plain Text : " + plainText)
    print("Cipher Text : " + cipherText)

    plainText = decrypt(cipherText, shift)
    print("\nDecryption") 
    print("Cipher Text : " + cipherText)
    print("Plain Text : " + plainText)

main()

