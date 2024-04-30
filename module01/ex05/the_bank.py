from types import coroutine


class Account:

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, "value"):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank:
    """The Bank"""

    def __init__(self):
        self.accounts = []


    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account:  Account() new account to append
            @return   True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            return False
        for account in self.accounts:
            if account.name == new_account.name:
                return False
        self.accounts.append(new_account)
        return True

    def is_corrupted(self, account):
        corruptions = []
        attrs = dir(account)

        if len(attrs) % 2 == 0:
            corruptions.append(1)
        for a in attrs:
            if a.startswith("b"):
                corruptions.append(2)
        if attrs.count("zip") == 0 and attrs.count("addr") == 0:
            corruptions.append(3)

        return corruptions

    def transfer(self, origin, dest, amount):
        """ Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
        """
        if origin == dest:
            return True
        else:
            transfered = 0
            for account in self.accounts:
                if origin == account.name:
                    if self.is_corrupted(account):
                        return False
                    if account.value >= amount:
                        account.value -= amount
                        transfered = 1
                if dest == account.name and transfered == 1:
                    if self.is_corrupted(account):
                        return False
                    account.value += amount
                    return True
            return False

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name:   str(name) of the account
            @return  True if success, False if an error occured
        """
        print("Encule")
        for account in self.accounts:
            corruptions = self.is_corrupted(account)
            print(account.name, name)
            if account.name == name and len(corruptions) > 0:
                print(corruptions)
                for corruption in corruptions:
                    if corruption == 1:
                        deletable = [x for x in dir(account) if not x.startswith("__") and x not in ["zip", "addr", "name", "id", "ID_COUNT", "value", "transfer"]]
                        print("Even nbr of attribute corruption detected. Choose which attribute to delete between those: ")
                        delattr(account, str(input(f"{deletable}: \n").strip()))
                        continue
                    if corruption == 2:
                        print("Corruption detected. Attribute starting with 'b'. Please delete it: ")
                        deletable = [x for x in dir(account) if x.startswith("b")]
                        delattr(account, str(input(f"{deletable}: \n").strip()))
                        continue
                    if corruption == 3:
                        print("Corruption detected. No zip or addr attribute. Please add one: ")
                        infos = str(input("Usage example: zip 'your zip code'\n")).split(" ")
                        setattr(account, infos[0], infos[1])
                        continue
                corruptions = []
                return True
            else:
                return False



def main():
    acc1 = Account(name="Dorian", value=100, jack=2, dax=3, dramcj="3", zip="1000", addr="Rue Loin")
    acc2 = Account(name="G", value=20, jack=2, dax=3, bon="3", zip="1000", addr="Rue Loin")
    la_banque = Bank()
    la_banque.add(acc1)
    la_banque.add(acc2)

    transfered = la_banque.transfer("Dorian", "G", 100)
    if not transfered:
        print(transfered)
        if la_banque.is_corrupted(acc1):
            print("Dorian oui")
            la_banque.fix_account("Dorian")
        elif la_banque.is_corrupted(acc2):
            print("G oui")
            la_banque.fix_account("G")
            print("FDP")
    transfered = la_banque.transfer("Dorian", "G", 100)
    print(transfered)

if __name__ == "__main__":
    main()
