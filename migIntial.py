import mysql.connector
import datetime
cur_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#print(cur_time)

# connection
db_org = mysql.connector.connect(host="localhost",user="root",passwd="",database="dbmasked")
db_copy = mysql.connector.connect(host="localhost",user="root",passwd="",database="test")
c_org=db_org.cursor()
c_copy=db_copy.cursor()

# taking last update from lookup
c_copy.execute('select migrate_time from lookup where company = "zen music" ')
lastupdate=c_copy.fetchall()
#print(lastupdate[0][0])

#taking values updated after lastupdate from orginal table
query_str1="select * from tblprospects where P_LASTUPDATED > '{lupdate}' "
query_str2=query_str1.format(lupdate=lastupdate[0][0]);
#print(query_str2)
c_org.execute(query_str2)
datatoinsert=c_org.fetchall()
'''print(type(datatoinsert))
print(type(datatoinsert[0]))
print(len(datatoinsert))
print(datatoinsert[0][0])'''

#inserting and updating data in copy table
for i in datatoinsert:
    query_str1="if exists(SELECT * from prospect where P_ID = {val1} ) THEN UPDATE prospect SET P_NAME = '{val2}' ,P_NO = '{val3}',P_SOURCE ='{val4}',P_INSTRUMENTS='{val5}',P_COMMENT='{val6}',P_DATEOFINQUIRY='{val7}',P_ALTERNATENUMBER='{val8}',P_ADDRESS='{val9}',P_LOCATION='{val10}',P_STATUS='{val11}',P_LASTUPDATED ='{val12}',P_DATEOFREMINDER ='{val13}', P_LASTINTERACTED = '{val14}',P_PREFFEREDLANGUAGE = '{val15}' WHERE P_ID = {val1}; ELSE insert into prospects values ({val1},'{val2}','{val3}','{val4}','{val5}','{val6}','{val7}','{val8}','{val9}','{val10}','{val11}','{val12}','{val13}','{val14}','{val15}'); END IF; "
    query_str2=query_str1.format(val1=i[0],val2=i[1],val3=i[2],val4=i[3],val5=i[4],val6=i[5],val7=i[6],val8=i[7],val9=i[8],val10=i[9],val11=i[10],val12=i[11],val13=i[12],val14=i[13],val15=i[14])
    #print(y)
    c_copy.execute(query_str2)

#updating time in lookup
query_str1="update lookup set migrate_time='{val}' where company='zen music'"
query_str2=query_str1.format(val = cur_time)
c_copy.execute(query_str2)
