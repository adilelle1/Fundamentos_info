from client import Client
from cards import DebitCard, CreditCard

CATEGORY_GOLD = 'Gold'
CATEGORY_PLATINUM = 'Platinum'
CATEGORY_BLACK = 'Black'

debitcard = DebitCard('1234 4245 2345 3456', CATEGORY_PLATINUM, '05/22', '05/25', '833')

cli1 = Client('Martin', 'Coronado', '+54 11 64455432', '35888229', 'La pampa 1234', CATEGORY_GOLD, debitcard)

creditcard = CreditCard('1234 4245 2345 3943', CATEGORY_PLATINUM, '05/22', '05/25', '843', 5555)

cli1.add_credit_card(creditcard)

cli1.__str__()
