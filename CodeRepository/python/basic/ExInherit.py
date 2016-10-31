#!/usr/bin/python
#-*- coding:utf-8 -*-
#早期版本python中，默认只支持显示ascii码，要添加上面那一行才不会出现报警信息：Non-ASCII character...
#Filename: ExInherit.py
#python类继承练习

import time

class SchoolMember:
    '''Represent any shcool member'''
    population = 0 #相当于static类成员
    
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        SchoolMember.population += 1  #refer to class static member
        print '(Initialized School Member: %s)'% self.name
    
    def tell(self):
        '''Tell my detailed info.'''
        print 'Name:"%s" Age:"%s"'% (self.name, self.age)
    
    def __del__(self):
        '''Destructor'''
        SchoolMember.population -= 1
        print 'Delete the member:%s'% self.name
        print 'populations :"%d"'% SchoolMember.population
        

    def howMany(self):
        print 'Hi, %s, There are "%d" members in school'% (self.name,SchoolMember.population)
        

class Teacher(SchoolMember):
    '''Represent a techear'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self, name, age) #python 不对自动调用基类的constructor
        self.salary = salary
        print '(Initialized a Teacher:%s'% self.name
    
    def tell(self):
        SchoolMember.tell(self)
        print 'Salary:"%d"'% self.salary


class  Student(SchoolMember):   
    '''Represent a student'''
    def __init__(self, name, age, mark):
        SchoolMember.__init__(self, name, age)
        self.mark = mark
        print '(Initialized a student:%s'% self.name
    
    def tell(self):
        SchoolMember.tell(self)
        print 'Mark: "%d"'% self.mark

t = Teacher('Mrs. Li', 40, 30000)
s = Student('Mr. Ma', 18, 98)

print #print a blank line

members = [t,s]

for member in members:
    member.tell()  #work for Both Teachers and Students

t.howMany()
del t
time.sleep(1) #sleep two seconds.
s.howMany() #这里还是显示有两个用户
del s
