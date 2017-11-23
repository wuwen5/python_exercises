# -*- coding: utf-8 -*-
# @author wenwu (wuwen dot 55 at gmail dot com)
import math

# 已知运算连接符
symbol = ['+', '-', '*', '/', '%', '>>', '<<']


def sqrt3(n):
    return n ** (1. / 3)


num_symbol = ['', math.sqrt, sqrt3]

format_math_function = {math.sqrt: '√', sqrt3: '3√', '': ''}


def calc(x, y, s):
    return eval('%s%s%s' % (x, s, y))


def exp_calc(x, r):
    for first_op in symbol:
        for second_op in symbol:
            try:
                for np in num_symbol:
                    if np:
                        n = np(x)
                    else:
                        n = x

                    ret = calc(calc(n, n, first_op), n, second_op)
                    if ret == r:
                        print format_math_function[np], x, first_op, format_math_function[
                            np], x, second_op, format_math_function[np], x, '=', ret
                        return ret
                    ret = calc(n, calc(n, n, second_op), first_op)
                    if ret == r:
                        print format_math_function[np], x, first_op, '(', format_math_function[
                            np], x, second_op, format_math_function[np], x, ')', '=', ret
                        return ret
            except Exception:
                continue


##解题  x ? x ? x = 6
print '题:'
for i in range(2, 10):
    print i, ' ', i, ' ', i, '=', '6'

print '解:'
for i in range(2, 10):
    exp_calc(i, 6)
