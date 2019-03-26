from variant1.yl4 import debt


def test(input_value, expected_result):
    actual_result = debt(*input_value)
    print('expected: %s, actual: %s' % (expected_result, actual_result))


test((3, 1, 3), 3)
test((1, 1, 1), 0)
test((2, 1, 3), 0)
test((1, 3, 3), 0)
test((1, 2, 2), 0)
test((0, 2, 2), -2)
test(('', 2, 2), None)
test((None, 2, 2), None)
