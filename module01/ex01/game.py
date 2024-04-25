class GotCharacter:
    def __init__(self, first_name: str, is_alive: bool = True):
        if not isinstance(first_name, str) or not first_name:
            raise ValueError("first name should be a non-empty string")
        if not isinstance(is_alive, bool) or not is_alive:
            raise ValueError("is alive should be a boolean")

        self.first_name = first_name
        self.is_alive = is_alive

        def __str__(self):
            return f"I am {self.first_name}"


class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name, is_alive)
        self.first_name = "Stark"
        self.house_words = "Winter is coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
