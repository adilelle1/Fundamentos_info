#Ejercicio 6 - Unidad 3

customer_payments = [
    '23423',
    '58092',
    '75230',
    '72879',
    '82231',
    '35465',
    '30943',
    '12772'
]


cards_trx = [
{'user_id': '35465', 'total_amount': 30000, 'payment_method':
'credit card', 'total_installments': 12, 'current_installment':
7},
{'user_id': '23423', 'total_amount': 19099, 'payment_method':
'credit card', 'total_installments': 12, 'current_installment':
3},
{'user_id': '82312', 'total_amount': 15500, 'payment_method':
'credit card', 'total_installments': 12, 'current_installment':
4},
{'user_id': '29332', 'total_amount': 90200, 'payment_method':
'credit card', 'total_installments': 6, 'current_installment':
4},
{'user_id': '82231', 'total_amount': 29000, 'payment_method':
'credit card', 'total_installments': 12, 'current_installment':
9},
{'user_id': '76289', 'total_amount': 42300, 'payment_method':
'credit card', 'total_installments': 12, 'current_installment':
11},
{'user_id': '58092', 'total_amount': 18900, 'payment_method':
'credit card', 'total_installments': 6, 'current_installment':
1},
{'user_id': '30943', 'total_amount': 13520, 'payment_method':
'debit card'},
{'user_id': '75230', 'total_amount': 67000, 'payment_method':
'credit card', 'total_installments': 6, 'current_installment':
4}, {'user_id': '20582', 'total_amount': 21500, 'payment_method':
'credit card', 'total_installments': 12, 'current_installment':
6},
{'user_id': '10943', 'total_amount': 5200, 'payment_method':
'debit card'},
{'user_id': '29002', 'total_amount': 9000, 'payment_method':
'credit card', 'total_installments': 12, 'current_installment':
11},
{'user_id': '92389', 'total_amount': 39200, 'payment_method':
'debit card'},
{'user_id': '12772', 'total_amount': 65700, 'payment_method':
'credit card', 'total_installments': 12, 'current_installment':
10},
{'user_id': '72879', 'total_amount': 7300, 'payment_method':
'credit card', 'total_installments': 6, 'current_installment':
5},
{'user_id': '83489', 'total_amount': 44000, 'payment_method':
'debit card'},
]

remaining_installment = 0

for i in cards_trx:
    for key,value in i.items():
        if value in customer_payments and 'current_installment' in i:
            print('Usuario: ', i.get('user_id'))
            print('Current installment original', i.get('current_installment'))
            i['current_installment']+=1
            print('Current installment actualizado', i.get('current_installment'))
            print('----')


