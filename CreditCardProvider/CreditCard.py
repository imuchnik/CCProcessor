class CreditCard:
    """A consumer credit card."""

    def init(self, customer, bank, card_number, limit):
        """Create a new credit card instance.The initial balance is zero. Customer the name of the customer (Lisa) and credit limit """

        self.customer = customer
        self.card_number = card_number
        self.limit = limit
        self.balance = 0


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
