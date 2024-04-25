kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}


def is_valid_dict(kata_to_check):
    if type(kata_to_check) is not dict:
        print("Kata datatype should be a dictionary")
        exit(1)
    for i in kata_to_check.items():
        if type(i[0]) is not str or type(i[1]) is not str:
            print("Kata keys and values not a string")
            exit(1)


def main():
    is_valid_dict(kata)
    for language, creator in kata.items():
        print(f"{language} was created by {creator}")


if __name__ == "__main__":
    main()
