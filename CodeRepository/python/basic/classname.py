# -*- coding: utf-8 -*-
class FooClass(object):
        """my very first class: FooClass"""
        version = 0.1  # class (data) attribute
        __privatevar = 3  # 双下划线开始的数据成员表示是 私有变量,不能被类对象访问
        _protectedvar = 5  # 建议，已单下划线开始的数据成员 表示为只能被本类对象访问

        def __init__(self, nm='John Doe'):
                """constructor"""
                self.name = nm  # class instance (data) attribute
                print '----- Created a class instance for', nm

        def __del__(self):
                print '----destruct this object'

        def __str__(self):
                """ toString() """
                return "_protectedvar=" + self.name

        def showname(self):
                """display instance attribute and class name"""
                print 'Your name is', self.name
                print 'My name is', self.__class__.__name__

        def showver(self):
                """display class(static) attribute"""
                print self.version  # references FooClass.version

        def addMe2Me(self, x):  # does not use 'self'
                """apply + operation to argument"""
                return x + x

        def staticmethod(self):  # non-static
            print "invoke a static method, which belongs to the class FooClass, not the instance!"



fool = FooClass()
print fool.showname()
print '-----'
print fool.version  # 公共的变量
# print fool.__privatevar 无法访问
print '-----'
foll = FooClass('Yoson')
print fool.showname()

print '-----'
print FooClass().addMe2Me(3)

print FooClass().staticmethod()

print FooClass('ma')