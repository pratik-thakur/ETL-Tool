# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 02:31:10 2020

@author: mahipal
"""

import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="abc")
myc=mydb.cursor()
myc.execute("select * from xyz")
result = myc.fetchall()
print(result)
myd = mysql.connector.connect(host="localhost",user="root",passwd="",database="test")
mycd=myd.cursor()
'''
for i in result:
   # print(i)
   # x='{f1} {f1} {f2}'
    x="if exists(SELECT * from demo where id= {f1} ) THEN UPDATE demo SET name = {f1} WHERE id= {f1}; ELSE insert into demo(id,name,address) values ({f1},{f2},{f3}); END IF; "
    y=x.format(f1=i[0],f2=i[1],f3=i[2])
    #print(y)
    mycd.execute(y)
#s="insert into demo(id,name,address) values (%s,%s,%s)"
#mycd.executemany(s,result)
    '''
myc.execute("Insert into abc.xyz select * from test.demo ")    
#query_str2=query_str1.format(lupdate=lastupdate[0][0]);   
#insert into test.demo(id, name, address) select * from abc.xyz ON DUPLICATE KEY UPDATE name = VALUES(name),address =values(address)  
#SELECT * FROM test.demo as d LEFT JOIN abc.xyz as x ON d.id = x.id 
#DELETE d FROM test.demo as d LEFT JOIN abc.xyz as x ON d.id = x.id WHERE x.id IS NULL