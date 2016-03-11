import operator
from decimal import Decimal

CREDIT_ACTION = "Credit"

CHARGE_ACTION = "Charge"

DOLLAR_SIGN = "$"

ERROR = "error"


class CardProcessor:
    def __init__(self, input_lines):
        """Initialize data structures and kick off processing"""
        self.card_activity = {}
        for input_line in input_lines:
            self.process_entry(input_line)

    # From Wikipedia
    def luhn_checksum(self, card_number):
        """Check if card is Luhn10 checksum valid"""

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
        """Wrapper for checksum validation"""

        return self.luhn_checksum(card_number) == 0

    def process_entry(self, entry):
        """ Process each line and take appropriate action"""

        entry = entry.split(' ')
        action_map = {
            "Add": self.add,
            "Charge": self.process_transaction,
            "Credit": self.process_transaction,
        }
        action_map.get(entry[0])(entry)

    def add(self, entry):
        """ Add card to internal data structure, if the card number is valid"""

        action, name, cardNumber, limit = entry
        balance = 0
        # what happens if name is a duplicate.
        if self.is_luhn_valid(cardNumber):
            self.card_activity[name] = [cardNumber, Decimal(limit[1:]), balance]
        else:
            self.card_activity[name] = ERROR

    def process_transaction(self, entry):
        """ Process "Charge or Credit"""

        if (self.is_valid_entry(entry)):
            action, name, amount = entry
            cardNumber, limit, balance = self.card_activity[name]
            amount = Decimal(amount[1:])
            if action == CHARGE_ACTION:
                if not (balance + amount) > limit:
                    total = balance + amount
                else:
                    return
            elif action == CREDIT_ACTION:
                total = balance - amount

            self.card_activity[name] = [cardNumber, limit, total]
        else:
            pass

    def is_valid_entry(self, entry):
        """  Validate card number was valid when it was added    """

        return self.card_activity[entry[1]] != ERROR

    def display_statement(self):
        """ Print the final statement """

        for entry in sorted(self.card_activity, key=operator.itemgetter(0)):
            name = entry
            value = self.card_activity[entry] if self.card_activity[entry] == ERROR else DOLLAR_SIGN + str(self.card_activity[entry][2])
            print(name + ": " + value)
