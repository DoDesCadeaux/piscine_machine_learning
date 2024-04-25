from sys import argv
import string


def text_analyzer(text: str):
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    if len(text) == 0:
        print("What is the text to analyze?")
        return

    characters = 0
    u_letter = 0
    l_letter = 0
    punc = 0
    spaces = 0

    for c in text:
        if c in string.ascii_uppercase:
            u_letter += 1
        elif c in string.ascii_lowercase:
            l_letter += 1
        elif c in string.punctuation:
            punc += 1
        elif c in string.whitespace:
            spaces += 1
        characters += 1
    print(f"""The text contains {characters} character(s):
- {u_letter} upper letter(s)
- {l_letter} lower letter(s)
- {punc} punctuation mark(s)
- {spaces} space(s)""")


def main():
    if (len(argv) > 1 and argv[1] == "None") or len(argv) == 1:
        print("AssertionError: cannot be empty or None, please provide a String")
    elif len(argv) > 2:
        print("AssertionError: too many arguments")
    else:
        text_analyzer(argv[1])


if __name__ == "__main__":
    main()
