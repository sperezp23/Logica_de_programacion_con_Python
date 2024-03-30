RATES = {
    'EUR':{
        'USD':1/0.85,
        'CHF':1/0.86,
        'GBP':0.885,
    },
    'USD':{
        'EUR':0.85,
        'CHF':0.85/0.86,
        'GBP':0.85/0.885,
    },
    'CHF':{
        'EUR':0.86,
        'USD':0.86/0.85,
        'GBP':0.86/0.885,
    },
    'GBP':{
        'EUR':1/0.885,
        'USD':0.885/0.85,
        'CHF':0.885/0.86,
    }
}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """

    if (currency == 'RMB') or (amount[1]=='RMB'):
        return None
    else:
        return round(amount[0]*RATES[amount[1]][currency],0)

print(convert((100, "EUR"),'GBP'))
print(convert((100, "USD"),'EUR'))
print(convert((200, "CHF"),'EUR'))
print(convert((300, "GBP"),'EUR'))
print(convert((339, "EUR"),'GBP'))
print(convert((300, "RMB"),'EUR'))
