import operator
from decimal import Decimal


class CardProcessor:
    def __init__(self, lines):
        self.cardActivity = {}
        for line in lines:
            self.process_entry(line)

    # From Wikipedia
    def luhn_checksum(self, card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]

        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10

    def is_luhn_valid(self, card_number):
        return self.luhn_checksum(card_number) == 0

    def process_entry(self, entry):
        entry = entry.split(' ')
        action_map = {
            "Add": self.Add,
            "Charge": self.Charge,
            "Credit": self.Credit,
        }
        action_map.get(entry[0])(entry)

    def Add(self, entry):
        action, name, cardNumber, limit = entry
        balance = 0
        # what happens if name is a duplicate.
        if self.is_luhn_valid(cardNumber):
            self.cardActivity[name] = [cardNumber, Decimal(limit[1:]), balance]
        else:
            self.cardActivity[name] = "error"

    def Charge(self, entry):
        self.process_transaction(entry)

    def Credit(self, entry):
        self.process_transaction(entry)

    def process_transaction(self, entry):
        if (self.is_valid_entry(entry)):
            action, name, amount = entry
            cardNumber, limit, balance = self.cardActivity[name]
            amount = Decimal(amount[1:])
            if action == "Charge":
                if not (balance + amount) > limit:
                    total = balance + amount
                else:
                    return
            elif action == "Credit":
                total = balance - amount

            self.cardActivity[name] = [cardNumber, limit, total]
        else:
            pass

    def is_valid_entry(self, entry):
        return self.cardActivity[entry[1]] != "error"

    def display_statement(self):

        for entry in sorted(self.cardActivity, key=operator.itemgetter(0)):
            name = entry
            value = self.cardActivity[entry] if self.cardActivity[entry] == "error" else "$" + str(
                self.cardActivity[entry][2])
            print(name + ": " + value)