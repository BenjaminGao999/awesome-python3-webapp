# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     fn.py
   Description :
   Author :       benjamin
   date：          2018/7/17
-------------------------------------------------
   Change Activity:
                   2018/7/17:
-------------------------------------------------
"""
__author__ = 'benjamin'


# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# v = power(3)

# print(v)


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


# print(enroll('Bob', 'male'))


# enroll('Jobs', 'male', 7)

# enroll('Steve', 'male', city='tokyo')


# 可变参数

def calc(*numbers):
    sum2 = 0
    for n in numbers:
        sum2 = sum2 + n * n
    return sum2


# print(calc(1, 2, 3))


# 关键字参数
def person(name, age, **kwargs):
    print('name:', name, 'age:', age, 'other:', kwargs)


# person('keven', 20)
# person('keven', 20, city='hangzhou')
# person('keven', 20, gender='male', nickname='libai')
extra = {'city': 'Beijing', 'job': 'Engineer'}


# person('Gao', 23, **extra)


# 如果要限制关键字参数的名字，就可以用命名关键字参数，
# 例如，只接收city和job作为关键字参数。这种方式定义的函数如下：

def person2(name, age, *, city, job):
    print(name, age, city, job)

# person2('Jim', 20, city='NewYork', job='teacher')


# TypeError: person2() missing 1 required keyword-only argument: 'job'
# person2('Jim', 23, city='NewLand')


#在Python中定义函数，可以用必选参数、默认参数、# 可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：
# 必选参数、默认参数、可变参数、命名关键字参数和关键字参数。




