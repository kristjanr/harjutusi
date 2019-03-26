from variant1.yl3 import currency_exchange


def test(input_value, expected_result):
    actual_result = currency_exchange(input_value)
    print('expected: %s, actual: %s' % (expected_result, actual_result))


test({'AUD': 1.59, 'USD': 1.13, 'GBP': 0.85}, 'GBP')
test({'AUD': 0.0, 'USD': 1.13, 'GBP': 0.85}, 'AUD')
test({'USD': 0.85}, 'USD')
test(None, None)
test({}, None)
