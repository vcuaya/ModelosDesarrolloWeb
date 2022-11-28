from bitcash import Key


def createKey():
    # Creation of a new private key
    k = Key()

    # Export Key
    return k.to_wif()


def getAddress(key):
    # Import Key
    # k = Key('L3sWEbgAYHZxQR9VxMRf6KSgGshttTTtC8X91ucwvmEoEHCZS3qU')
    k = Key(key)

    # All keys possess an address() property which is derived from your public key
    # This is what you share with others to receive payments.
    text = k.address

    array = text.split(':', 1)
    return array[1]

def getBalance(key):
    # Import Key
    # k = Key('L3sWEbgAYHZxQR9VxMRf6KSgGshttTTtC8X91ucwvmEoEHCZS3qU')
    k = Key(key)

    # The current balance. This internal balance will always be in satoshi.
    # print(k.get_balance())

    # Optional argument currency Bitcoin Cash
    # print(k.get_balance('bch'))

    # Optional argument currency USD
    # print(k.get_balance('usd'))

    return float(k.get_balance('usd'))


def verifyPay(key, pay):
    # Balance before the transaction
    balance = getBalance(key)

    # New Balance after the transaction
    newBalance = getBalance(key)

    if(newBalance == balance + pay):
        return True
    else:
        return False


# Key
key = 'L3sWEbgAYHZxQR9VxMRf6KSgGshttTTtC8X91ucwvmEoEHCZS3qU'

# Pay to recieve
pay = 1

print('La dirección de la llave es: ', getAddress(key))
print('El saldo de la cuenta es: ', getBalance(key), 'USD')
print('Verificación del pago', verifyPay(key, pay))
