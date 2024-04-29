from collections.abc import Iterable


class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if isinstance(coefs, Iterable) and isinstance(words, Iterable):
            for c, w in zip(coefs, words):
                if not isinstance(c, (int, float)):
                    return -1
                if not isinstance(w, str):
                    return -1
        if len(coefs) != len(words) or not coefs or not words:
            return -1
        products = []
        for c, w in zip(coefs, words):
            products.append(len(w) * c)
        return sum(products)

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if isinstance(coefs, Iterable) and isinstance(words, Iterable):
            for c, w in zip(coefs, words):
                if not isinstance(c, (int, float)):
                    return -1
                if not isinstance(w, str):
                    return -1
        if len(coefs) != len(words) or not coefs or not words:
            return -1
        products = []
        for index, word in enumerate(words):
            products.append(len(word) * coefs[index])
        return sum(products)
        
def main():
    words = ["abc", "abcd", "a", "ab", "abcdef"]
    coefs = [1, 2, 1, 3, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))
    print(Evaluator.enumerate_evaluate(coefs, words))


if __name__ == "__main__":
    main()
