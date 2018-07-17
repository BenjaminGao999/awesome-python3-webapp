# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     student
   Description :
   Author :       benjamin
   date：          2018/7/16
-------------------------------------------------
   Change Activity:
                   2018/7/16:
-------------------------------------------------
"""
__author__ = 'benjamin'


class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


print(dir(Student))

jobs = Student('steve jobs', 23)

print(jobs.name)

print(jobs.age)

