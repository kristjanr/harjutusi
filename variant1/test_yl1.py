from variant1.yl1 import elements_sum


def test(input_value, expected_result):
    actual_result = elements_sum(input_value)
    print('expected: %s, actual: %s' % (expected_result, actual_result))


test(1, 1)
test(2, 3)
test(3, 6)
test(0, 0)
test(None, None)
