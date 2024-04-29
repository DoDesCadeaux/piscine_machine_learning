from random import randint

def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    """
    if not isinstance(text, str) and not text.isprintable():
        print("Error")
        exit(1)
    if option and option.strip() not in ["shuffle", "unique", "ordered"]:
        print("Error")
        exit(1)
    generate = text.split(sep)

    if option == "shuffle":
        i = 0
        for _ in generate:
            r = randint(0, len(generate) - 1)
            generate[i], generate[r] = generate[r], generate[i]
            i += 1
    elif option == "unique":
        generate = list(set(generate))
    elif option == "ordered":
        generate.sort()
    for w in generate:
        yield w


def main():
    text = "B cool je suis pas la, ah bon cest dorian euh non"
    for w in generator(text, sep=" ", option="shuffle"):
        print(w)


if __name__ == "__main__":
    main()

