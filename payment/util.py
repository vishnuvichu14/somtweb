from hashlib import sha512
from django.conf import settings

KEYS = ('txnid', 'amount', 'productinfo', 'firstname', 'email',
        'udf1', 'udf2', 'udf3', 'udf4', 'udf5', 'udf6', 'udf7', 'udf8',
        'udf9', 'udf10')


def generate_hash(data, ):
    # key = settings.PAYU_MERCHANT_KEY
    key = settings.PAYU_INFO['merchant_key']
    # salt = settings.PAYU_MERCHANT_SALT
    salt = settings.PAYU_INFO['merchant_salt']
    print(key,salt)
    txnid = data["txnid"]
    amount = data['amount']
    product_info = data['product_info']
    first_name = data['first_name']
    email = data["email"]
    print(txnid)
    hash_value = sha512(
        str("{}|{}|{}|{}|{}|{}|||||||||||{}").format(key, txnid, amount, product_info, first_name, email, salt).encode(
            "utf-8"))
    return hash_value.hexdigest().lower()


KEYS_MOBILE = ('txnid', 'amount', 'product_info', 'first_name', 'email',
               'udf1', 'udf2', 'udf3', 'udf4', 'udf5')


def generate_hash_mobile(data):
    hash_value = sha512(settings.PAYU_INFO.get('merchant_key'))
    for key in KEYS_MOBILE:
        hash_value.update("%s%s" % ('|', data.get(key, '')))

    hash_value.update("%s%s" % ('|', settings.PAYU_INFO.get('merchant_salt')))

    return hash_value.hexdigest().lower()


def verify_hash(data):
    reversed_keys = reversed(KEYS)
    if data.get('additionalCharges'):

        hash_value = sha512(data.get('additionalCharges'))
        hash_value.update("%s%s" % ('|', settings.PAYU_INFO.get('merchant_salt').encode("utf-8")))
    else:

        hash_value = sha512(settings.PAYU_INFO.get('merchant_salt').encode("utf-8"))

    hash_value.update(("%s%s" % ('|', str(data.get('status', '')))).encode('utf-8'))

    for key in reversed_keys:
        hash_value.update(("%s%s" % ('|', str(data.get(key, '')))).encode('utf-8'))

    hash_value.update(("%s%s" % ('|', settings.PAYU_INFO.get('merchant_key'))).encode('utf-8'))

    return hash_value.hexdigest().lower() == data.get('hash')
