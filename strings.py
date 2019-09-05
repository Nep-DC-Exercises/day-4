string = 'nep'

upper_string = string.upper()
print(upper_string)

cap_string = string.capitalize()
print(cap_string)

rev_string = string[::-1]
print(rev_string)

# Leetspeak Translator Exercise
normal_speak = 'Given a paragraph of text as as a string, print the paragraph in leetspeak. To translate a string to leetspeak, you need to make the following character replacements.'

normal_speak = normal_speak.upper()

leet_dict = {
    'A': '4',
    'E': '3',
    'G': '6',
    'I': '1',
    'O': '0',
    'S': '5',
    'T': '7'
}

leet_speak = ""

for letter in normal_speak:

    if letter in leet_dict:
        leet_speak += leet_dict.get(letter)
    else:
        leet_speak += letter

print(leet_speak)

# Output = 61V3N 4 P4R46R4PH 0F 73X7 45 45 4 57R1N6, PR1N7 7H3 P4R46R4PH 1N L3375P34K. 70 7R4N5L473 4 57R1N6 70 L3375P34K, Y0U N33D 70 M4K3 7H3 F0LL0W1N6 CH4R4C73R R3PL4C3M3N75.'''


# Long-long Vowels
# Given a word as a string, print the result of extending any long values to the length of 5
# long vowel  =  two vowels in a row

word = "good"
vowels = ["a", "e", "i", "o", "u"]
new_word = ""

'''Problem Solving Steps: 
1. Take a string. Loop through it and see if there are two sequential vowels
2. if there are two sequential vowels, add five of that letter to new_word
3. Add the remaining letters to new_word if they aren't sequential vowels
'''

for i in range(len(word)):

    if word[i] in vowels:

        if word[i] == word[i+1]:

            new_word += word[i] * 5

        else:
            new_word += word[i]
    else:
        new_word += word[i]

print(new_word)


# Caesar Cipher - Given a string, print the Caesar Cipher of that string.
encrypted_string = "lbh zhfg hayrnea jung lbh unir yrnearq"

alphabet = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
    8: 'i',
    9: 'j',
    10: 'k',
    11: 'l',
    12: 'm',
    13: 'n',
    14: 'o',
    15: 'p',
    16: 'q',
    17: 'r',
    18: 's',
    19: 't',
    20: 'u',
    21: 'v',
    22: 'w',
    23: 'x',
    24: 'y',
    25: 'z'
}

caesar_alphabet = {
    'a': 13,
    'b': 14,
    'c': 15,
    'd': 16,
    'e': 17,
    'f': 18,
    'g': 19,
    'h': 20,
    'i': 21,
    'j': 22,
    'k': 23,
    'l': 24,
    'm': 25,
    'n': 0,
    'o': 1,
    'p': 2,
    'q': 3,
    'r': 4,
    's': 5,
    't': 6,
    'u': 7,
    'v': 8,
    'w': 9,
    'x': 10,
    'y': 11,
    'z': 12
}

decoded_string = ""


def decipher(key):

    alphabet_key = caesar_alphabet.get(key, " ")
    decipher_string = alphabet.get(alphabet_key, " ")
    return decipher_string


for letter in encrypted_string:

    decoded_string += decipher(letter)

print(decoded_string)  # Output:  you must unlearn what you have learned
