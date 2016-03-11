import unittest
from unittest import TestCase

from CreditCardProvider.CardProcessor import CardProcessor


class TestCardProcessor(TestCase):
    def setUp(self):
        self.cardprocessor = CardProcessor([])

    def test_is_luhn_valid(self):
        self.assertFalse(self.cardprocessor.is_luhn_valid(1234567890123456))
        self.assertTrue(self.cardprocessor.is_luhn_valid(5454545454545454))

    def test_processEntry(self):
        self.cardprocessor.process_entry('Add Lisa 5454545454545454 $3000')
        self.assertEquals(len(self.cardprocessor.card_activity), 1)
        self.cardprocessor.process_entry('Charge Lisa $300')
        self.assertEquals(self.cardprocessor.card_activity['Lisa'][2], 300)

    def test_add(self):
        self.cardprocessor.add(['Add', 'Lisa', 5454545454545454, '$3000'])
        self.assertEquals(len(self.cardprocessor.card_activity), 1)

    def test_process_transaction(self):
        self.cardprocessor.add(['Add', 'Lisa', 5454545454545454, '$3000'])
        self.assertEquals(self.cardprocessor.card_activity['Lisa'][2], 0)
        self.cardprocessor.process_transaction(['Charge', 'Lisa', '$300'])
        self.assertEquals(self.cardprocessor.card_activity['Lisa'][2], 300)
        self.cardprocessor.process_transaction(['Credit', 'Lisa', '$100'])
        self.assertEquals(self.cardprocessor.card_activity['Lisa'][2], 200)
        self.cardprocessor.process_transaction(['Charge', 'Lisa', '$3000'])
        self.assertEquals(self.cardprocessor.card_activity['Lisa'][2], 200)

    def test_is_valid_entry(self):
        cardprocessor = CardProcessor(['Add Quincy 1234567890123456 $2000'])
        result = cardprocessor.is_valid_entry(["Foo", "Quincy"])
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
