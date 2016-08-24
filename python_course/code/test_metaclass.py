#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    return type(future_class_name, future_class_parents, uppercase_attr)

#在3.5.2 中被废弃
__metaclass__ = upper_attr

class Foo(object,metaclass=upper_attr):
    bar = 'bip'

print(dir(Foo))
print(dir(type))
print (hasattr(Foo, 'bar'))
print (hasattr(Foo, 'BAR'))
#f = Foo()
#print f.BAR

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList([])
L.add(1)
print(L)
