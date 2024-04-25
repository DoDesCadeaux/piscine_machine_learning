from sys import argv as av

MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ', ': '--..--', '.': '.-.-.-',
        '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-'
}


def check_isalnum(av):
    for i in av[1:]:
        if i.isupper():
            for j in i:
                if not j.isalnum() and not j.isspace():
                    print("ERROR")
                    exit(1)
        else:
            print("ERROR")
            exit(1)


def merge_args():
    if len(av) > 2:
        merged = []
        for i in av[1:]:
            merged.append(i)
        return merged
    elif len(av) == 1:
        exit(1)
    return [str(av[1])]


def encode_word(phrase):
    encoded = str()
    for w in phrase:
        for c in w:
            if c in MORSE_CODE_DICT:
                encoded += MORSE_CODE_DICT[c] + " "
            elif c == " ":
                encoded += "/ "
    return encoded


def encode(merged_args):
    encoded_msg = ""

    for w in merged_args:
        encoded_msg += encode_word(w) + " "
    print(encoded_msg.strip())


def main():
    check_isalnum(av)
    merged = merge_args()
    encode(merged)


if __name__ == "__main__":
    main()
