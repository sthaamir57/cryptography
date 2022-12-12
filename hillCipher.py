MATRIX_KEY = []
MATRIX_PLAINTEXT = []

def convertToIndex(m):
    for j in range (len(m)):
        for k in range (len(m[0])):
            m[j][k] = ord(m[j][k]) - 65

def convertToMatrix(matrix, text, K):
    for i in range (0, len(text), K):
        matrix.append(list(text[i: i + K]))
    convertToIndex(matrix)

def encrypt(KEY, PLAINTEXT):
    text = ''
    for i in range(len(PLAINTEXT)):
        el = ((KEY[0][0] * PLAINTEXT[i][0]) + (KEY[0][1] * PLAINTEXT[i][1])) % 26
        text += chr(el + 65)
        el2 = ((KEY[1][0] * PLAINTEXT[i][0]) + (KEY[1][1] * PLAINTEXT[i][1])) % 26
        text += chr(el2 + 65)
    return text

def main():
    plainText = 'SHORTEXAMPLE'
    key = 'HILL'

    # plainText = plainText.upper()
    # key = key.upper()

    if((len(plainText) % 2) != 0):
        plainText += 'Z';

    convertToMatrix(MATRIX_KEY, key, 2)
    convertToMatrix(MATRIX_PLAINTEXT, plainText, 2)

    cipher = encrypt(MATRIX_KEY, MATRIX_PLAINTEXT)
    
    print(cipher)


main()