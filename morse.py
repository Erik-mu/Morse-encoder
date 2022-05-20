morse_alpha = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    ' ':' '
}
morse_word  = []

print("Welcome to morse code encoder")
word = input("Type the word to encode in morse: ")
word_up = word.upper()
print(word_up)
letters = list(word_up)        #code -> c o d e
print(letters)

for letter in letters:
    morse = morse_alpha[letter]
    morse_word.append(morse)

print(morse_word)
