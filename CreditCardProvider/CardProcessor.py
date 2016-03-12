import operator
from decimal import Decimal
from CreditCard import CreditCard

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
        self.card_activity[name] = CreditCard(name, cardNumber, Decimal(limit[1:]))


    def process_transaction(self, entry):
        """ Process "Charge or Credit"""

        action, name, amount = entry
        amount = Decimal(amount[1:])
        if action == CHARGE_ACTION:
            self.card_activity[name].charge(amount)

        elif action == CREDIT_ACTION:
            self.card_activity[name].credit(amount)


    def display_statement(self):
        """ Print the final statement """

        for entry in sorted(self.card_activity, key=operator.itemgetter(0)):
            name = entry
            balance=str(self.card_activity[entry].get_balance())
            value = ERROR if balance==ERROR else DOLLAR_SIGN + str(balance)
            print(name + ": " + value)
