ERROR = "error"


class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, card_number, limit):
        """Create a new credit card instance.The initial balance is zero. Customer the name of the customer (Lisa) and credit limit """

        self.customer = customer
        if (self.is_luhn_valid(card_number)):
            self.card_number = card_number
            self.limit = limit
            self.balance = 0

        else:
            self.card_number = ERROR
            self.balance = ERROR

    def get_customer(self):
        """Return name of the customer."""

        return self.customer

    def get_account(self):
        """Return the card  number."""
        return self.card_number

    def get_limit(self):
        """Return current credit limit."""
        return self.limit

    def get_balance(self):
        """Return current balance."""
        return self.balance

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

    def charge(self, amount):
        """ Adds charge to the credit card"""

        if self.is_valid_entry() and not (self.balance + amount) > self.limit:
                    self.balance = self.balance + amount;
        else:
            return

    def credit(self, amount):
        """Applies credit to the balance"""
        if  self.is_valid_entry():
            self.balance = self.balance - amount

    def is_valid_entry(self):
        """  Validate card number was valid when it was added    """
        return self.card_number != ERROR

