import unittest
from unittest import TestCase

from CreditCardProvider.CardProcessor import CardProcessor


class TestCardProcessor(TestCase):
    def setUp(self):
        self.cardprocessor = CardProcessor([])

    def test_processEntry(self):
        self.cardprocessor.process_entry('Add Lisa 5454545454545454 $3000')
        self.assertEquals(len(self.cardprocessor.card_activity), 1)

    def test_add(self):
        self.cardprocessor.add(['Add', 'Lisa', 5454545454545454, '$3000'])
        self.assertEquals(len(self.cardprocessor.card_activity), 1)

    def test_create_with_zero_balance(self):
        self.cardprocessor.add(['Add', 'Lisa', 5454545454545454, '$3000'])
        self.assertEquals(self.cardprocessor.card_activity['Lisa'].get_balance(), 0)

    def test_card_charge(self):
        self.cardprocessor.add(['Add', 'Lisa', 5454545454545454, '$3000'])
        self.cardprocessor.process_transaction(['Charge', 'Lisa', '$300'])
        self.assertEquals(self.cardprocessor.card_activity['Lisa'].get_balance(), 300)

    def test_card_credit(self):
        self.cardprocessor.add(['Add', 'Lisa', 5454545454545454, '$300'])
        self.cardprocessor.process_transaction(['Credit', 'Lisa', '$200'])
        self.assertEquals(self.cardprocessor.card_activity['Lisa'].get_balance(), -200)

    def test_card_over_limit(self):
        self.cardprocessor.add(['Add', 'Lisa', 5454545454545454, '$300'])
        self.cardprocessor.process_transaction(['Charge', 'Lisa', '$400'])
        self.assertEquals(self.cardprocessor.card_activity['Lisa'].get_balance(), 0)

    def test_create_error_aacount(self):
        cardprocessor = CardProcessor(['Add Quincy 1234567890123456 $2000'])
        self.assertTrue(cardprocessor.card_activity['Quincy'].get_balance()=="error")


if __name__ == '__main__':
    unittest.main()
