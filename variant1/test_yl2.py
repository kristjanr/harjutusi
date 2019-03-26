from math import inf

from variant1.yl2 import total_amount


def test(input_value, expected_result):
    actual_result = total_amount(*input_value)
    print('expected: %s, actual: %s' % (expected_result, actual_result))


test((100, 10, 22), 814)
test((1, 0, 1000), 1)
test((0, 1000, 1000), 0)
test((1000, 1000, 1000), inf)
test((1000, 1000, 10), 25937424601000)
test((None, 1000, 10), None)
test(('foo', 1000, 10), None)
