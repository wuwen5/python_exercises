# -*- coding: utf-8 -*-
# @author wenwu (wuwen dot 55 at gmail dot com)
import math

# 已知运算连接符 ##补充 '>>', '<<', '&', '|'
symbol = ['+', '-', '*', '/', '%']


def sqrt3(n):
    return n ** (1. / 3)


num_symbol = ['', math.sqrt, sqrt3]

format_math_function = {math.sqrt: '√', sqrt3: '3√', '': ''}

def num_group():
    list = []
    for x in num_symbol:
        for y in num_symbol:
            for z in num_symbol:
                list.append([x, y, z])
    return list


def exp_calc(x, r):
    for first_op in symbol:
        for second_op in symbol:
            try:
                for tp in num_group():
                    source = '%s%s%s%s%s' % ('%s', first_op, '%s', second_op, '%s')
                    ret = eval(
                        source % tuple([tp[0](x) if tp[0] else x, tp[1](x) if tp[1] else x, tp[2](x) if tp[2] else x]))
                    if ret == r:
                        print '%s' * 10 % (format_math_function[tp[0]],x,first_op,format_math_function[tp[1]],x,second_op,format_math_function[tp[2]],x,'=',ret)
            except Exception:
                continue


##解题  x ? x ? x = 6


print '题:'
for i in range(2, 10):
    print i, ' ', i, ' ', i, '=', '6'

print '解:'
for i in range(2, 10):
    print '*' * 30
    exp_calc(i, 6)
