from datetime import datetime

kata = (2019, 9, 25, 3, 30)


def format_kata(kata_to_format):
    try:
        obj = datetime(*kata_to_format)  # Le * va déballer tous les élements de la tuple
        print(f"{obj.strftime('%m/%d/%Y %H:%M')}")
    except ValueError:
        print("Values out of range")
        exit(2)


def main():
    format_kata(kata)


if __name__ == "__main__":
    main()
