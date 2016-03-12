# Basic Credit Card Processing

## Overview/Design Decision

1. **_Language_** - I played and implemented the solution in a couple of other languages ( groovy, nodejs), but in the end liked python the 
     most and settled on it as my choice. I chose python because it is both well suited as a scripting language (for runnning as an executable)
     as well as supporting object oriented design, allowing for separation of concerns. In addition, it has nice libraries for processing
     command line args, has robust testing support and lends itself well to readability. 
     
2. **_Design decisions_** - the exersize is pretty straight forward. I have divided it into 3 concrete functions:
<br/>
* **CCProcessorScript.py** - is an executable file, that ingests command line arguments (or STDIN, parses the the input and provides it 
to CreditCardProcessor class in the format that is expected. It also calls for display function to print out the result. 

* **CreditCard.py** - Credit card account abstraction. Handles all card functions and transactions. Separated to for modularity, reuse 
    and better code organization

* **CardProcessor.py** - Responsible for processing each entry of the input,invoke apporopriate action,
     keep session state and display the result. 

* I chose a simple Hash table  as a data structure to keep track of current active cards. The key is the customer name. 
This desicsion is dictated by the input example. The credit and charges  provide only a name as means of locating the card account. 
    

## Dependencies
 ~Python 2.7
 All the other dependendencies are included with Python. No additional dependencies need to be installed. 

## To Run:

1. cd braintree/CreditCardProvider
2. Make sure CCProcessorScript is executable
3. ```./CCProcessorScript.py path/to/file or ./CCProcessorScript.py<path/to/file``` 


## To Run Tests

```
 python -m unittest discover -v

```

Imagine that you're writing software for a credit card provider. Implement a
program that will add new credit card accounts, process charges and credits
against them, and display summary information.

## Requirements:

- Your program must accept input from two sources: a filename passed in
command line arguments and STDIN. For example, on Linux or OSX both
'./myprogram input.txt' and './myprogram < input.txt' should work.
- Your program must accept three input commands passed with space delimited
arguments.
- "Add" will create a new credit card for a given name, card number, and limit
- Card numbers should be validated using Luhn 10
- New cards start with a $0 balance
- "Charge" will increase the balance of the card associated with the provided
name by the amount specified
- Charges that would raise the balance over the limit are ignored as if they
were declined
- Charges against Luhn 10 invalid cards are ignored
- "Credit" will decrease the balance of the card associated with the provided
name by the amount specified
- Credits that would drop the balance below $0 will create a negative balance
- Credits against Luhn 10 invalid cards are ignored - ???? 
- When all input has been read and processed, a summary should be generated and
written to STDOUT.
- The summary should include the name of each person followed by a colon and
balance
- The names should be displayed alphabetically
- Display "error" instead of the balance if the credit card number does not pass
Luhn 10

## Input Assumptions:

- All input will be valid -- there's no need to check for illegal characters
or malformed commands.
- All input will be space delimited
- Credit card numbers may vary in length up to 19 characters
- Credit card numbers will always be numeric
- Amounts will always be prefixed with "$" and will be in whole dollars (no
decimals)

## Example Input:

```
Add Tom 4111111111111111 $1000
Add Lisa 5454545454545454 $3000
Add Quincy 1234567890123456 $2000
Charge Tom $500
Charge Tom $800
Charge Lisa $7
Credit Lisa $100
Credit Quincy $200
```

## Example Output:

```
Lisa: $-93
Quincy: error
Tom: $500
```

Implement your solution in any programming language you wish, but keep in mind
we may ask you to explain or extend your code. Please write automated tests
and include them with your submission.

In addition to your code and tests, please also include a README that explains:

- An overview of your design decisions
- Why you picked the programming language you used
- How to run your code and tests, including how to install any dependencies
your code may have.

Thank you!

**Note: this information is confidential. It is prohibited to share, post online
or otherwise publicize without Braintree's prior written consent.**

