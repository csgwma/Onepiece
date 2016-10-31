# coding=utf-8
__author__ = 'Ace'


import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='adminadmin', db='test', port=3306)
    cur = conn.cursor()
    result = cur.execute('select * from student')  # 等于返回的行数
    print 'result = ', result
    for row in cur.fetchall():
        print '%s\t%s\t%s\t%s' % row

    # VALUES()字段必须完全匹配，蛋疼
    result = cur.execute("insert into student VALUES(8,'zhang',19,'2014-01-01 00:03:56')")
    print 'result = ', result

    result = cur.execute("delete from student WHERE id = 8")  # VALUES()字段必须完全匹配，蛋疼
    print 'result = ', result



    ids = [9, 10]
    names = ['hao', 'qiu']
    ages = [29, 28]
    print (ids, names)

    lists = [('9', 'hao', '29'), ('10', 'qiu', '28')]
    result = cur.executemany("insert into student VALUES(?,?,?,'2014-01-01 00:03:56')", lists)

    for row in cur.fetchall():
        print '%s\t%s\t%s\%s' % row

    cur.close()
    conn.commit()
    conn.close()
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])


print 'over'