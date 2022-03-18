# coding: utf-8
from collections import Counter
import copy
import re
import argparse
import sys

import ast
import operator as op

# supported operators
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.floordiv, 
             ast.USub: op.neg}

def eval_expr(expr):
    """
    >>> eval_expr('2^6')
    4
    >>> eval_expr('2**6')
    64
    >>> eval_expr('1 + 2*3**(4^5) / (6 + -7)')
    -5.0
    """
    return eval_(ast.parse(expr, mode='eval').body)

def eval_(node):
    if isinstance(node, ast.Num): # <number>
        return node.n
    elif isinstance(node, ast.BinOp): # <left> <operator> <right>
        if isinstance(node.op, ast.Div):
            if (eval_(node.left) % eval_(node.right))==0:
                return operators[type(node.op)](eval_(node.left), eval_(node.right))
            else:
                #return 0
                raise TypeError(node)
        else:
            return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)



# nerdle = 8 slots = 2 operations
# nerle mini = 6 slots = 1 operation

# number from 1 to 99
# ops in + - * /

# create operation and compute result
# rule on * temrs inc order ?
# check that it fits the right number characters


if True:
    for n1 in range(1,999):
        for n2 in range(1,999):
            for op in ['+','-','*','/']:
                line = str(n1)+op+str(n2)
                try:
                    line += "="+str(eval_expr(line))
                    if len(line)==8:
                        print(line)
                except TypeError:
                    pass

if False:
    for n1 in range(1,9999):
        for n2 in range(1,99):
            for op in ['+','-','*','/']:
                line = str(n1)+op+str(n2)
                try:
                    line += "="+str(eval_expr(line))
                    if len(line)==9:
                        print(line)
                except TypeError:
                    pass

if False:
    for n1 in range(1,99):
        for n2 in range(1,99):
            for n3 in range(1,99):
                for op1 in ['+','-','*','/']:
                    for op2 in ['+','-','*','/']:
                        line = str(n1)+op1+str(n2)+op2+str(n3)
                        try:
                            line += "="+str(eval_expr(line))
                            if len(line)==8:
                                print(line)
                        except TypeError:
                            pass

if False:
    for n1 in range(1,99):
        for n2 in range(1,99):
            for n3 in range(1,99):
                for op1 in ['+','-','*','/']:
                    for op2 in ['+','-','*','/']:
                        line = str(n1)+op1+str(n2)+op2+str(n3)
                        try:
                            line += "="+str(eval_expr(line))
                            if len(line)==9:
                                print(line)
                        except TypeError:
                            pass
