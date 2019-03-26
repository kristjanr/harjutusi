from variant1.yl6 import list_sum


def test(input_value, expected_result):
    actual_result = list_sum(input_value)
    print('expected: %s, actual: %s' % (expected_result, actual_result))


test([1, 2, 3], 6)
test([10000000, 2.12312, 3], 10000005.12312)
test([0, 0, 0], 0)
test([0, 0, ''], 0)
test([1, 1, ''], 2)
test(None, None)
test('sadsa', None)
