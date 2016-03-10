#! /bin/sh
""":"
exec python $0 ${1+"$@"}
"""

import sys
import operator
from decimal import Decimal

cardActivity = {}

def readFileAndSplitLines():
    with open(sys.argv[1], 'r') as file:
        contents = file.read()

        return contents.splitlines()

# From Wikipedia
def luhn_checksum(card_number):
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


def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0


def processEntry(entry):
    entry = entry.split(' ')
    action_map = {
        "Add": Add,
        "Charge": Charge,
        "Credit": Credit,
    }
    action_map.get(entry[0])(entry)


def Add(entry):
    action, name, cardNumber, limit = entry
    balance = 0
    # what happens if name is a duplicate.
    if is_luhn_valid(cardNumber):
        cardActivity[name] = [cardNumber, Decimal(limit[1:]), balance]
    else:
        cardActivity[name] = "error"


def Charge(entry):
    process_transaction(entry)


def Credit(entry):
    process_transaction(entry)


def process_transaction(entry):
    if (is_valid_entry(entry)):
        action, name, amount = entry
        cardNumber, limit, balance = cardActivity[name]
        amount = Decimal(amount[1:])
        if action == "Charge":
            if not (balance + amount) > limit:
                total = balance + amount
            else:
                return
        elif action == "Credit":
            total = balance - amount

        cardActivity[name] = [cardNumber, limit, total]
    else:
        pass


def is_valid_entry(entry):
    return cardActivity[entry[1]] != "error"

if len(sys.argv)>1:
    entries = readFileAndSplitLines()
else:
    entries =sys.stdin.readlines()

for entry in entries:
    processEntry(entry)

for entry in sorted(cardActivity, key=operator.itemgetter(0)):
    name = entry
    value = cardActivity[entry] if cardActivity[entry] == "error" else "$" + str(cardActivity[entry][2])
    print(name + ": " + value)



