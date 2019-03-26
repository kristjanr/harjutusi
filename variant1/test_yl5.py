from variant1.yl5 import liblikas


def test(input_value, expected_result):
    actual_result = liblikas(input_value)
    print('expected: %s actual: %s' % (expected_result, actual_result))
    equals = expected_result == actual_result
    print('does expected equal actual?: %s' % equals)


test('Kui Arno isaga koolimajja jõudis',
     'Kui liblikas isaga koolimajja jõudis')

test('Kui Arno isaga koolimajja jõudis, olid tunnid juba alanud',
     'Kui Arno isaga koolimajja jõudis, olid tunnid juba liblikas')

test('Kui Arno isaga koolimajja jõudis, olid tunnid juba alanud ja alanud ja alanud',
     'Kui Arno isaga koolimajja jõudis, olid tunnid juba alanud ja alanud ja liblikas')

test('a', 'liblikas')
test('a a', 'a liblikas')
test('', '')
test('0', '0')
test(None, None)
test(0, None)
