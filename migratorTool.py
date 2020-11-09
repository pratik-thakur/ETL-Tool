import mysql.connector
import datetime
import smtplib
import xml.etree.ElementTree as et

cur_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #print(cur_time)
    
def mail(body):
    s = smtplib.SMTP('smtp.gmail.com', 587)  
    s.starttls() 
    s.login("sender_email_id", "sender_email_id_password") 
   # message = "Message_you_need_to_send"
    subject="Error occured while running Etl tool"
    msg = f'Subject:{subject}\n\n{body}'
    s.sendmail("sender_email_id", "receiver_email_id", msg)  
    s.quit() 

def file(msg):
    f=open("log.txt","a")
    f.write(cur_time)
    f.write(str(msg))
    f.close()    

try:
    
    #xml file prassing getting root element
    tree =et.parse('query.xml')
    root =tree.getroot()
    
    # connection
    db_org = mysql.connector.connect(host="localhost",user="root",passwd="",database="dbmasked")
    db_copy = mysql.connector.connect(host="localhost",user="root",passwd="",database="test")
    c_org=db_org.cursor()
    c_copy=db_copy.cursor()
    
    # taking last update from lookup
    c_copy.execute('select migrate_time from lookup where company = "zen music" ')
    lastupdate=c_copy.fetchall()
    #print(lastupdate[0][0])
    
    for qry in root:
            #inserting and updating all the values
        query_str1=qry[0].text
        query_str2=query_str1.format(lupdate=lastupdate[0][0]);
            #print(query_str2)
        c_copy.execute(query_str2)
        #print("done")
            #deleting old entries
        query_str1=qry[1].text
        c_copy.execute(query_str1)
        #print("done")
    
    #updating time in lookup
    query_str1="update lookup set migrate_time='{val}' where company='zen music'"
    query_str2=query_str1.format(val = cur_time)
    c_copy.execute(query_str2)
    
except mysql.connector.Error as err:
    db_org.rollback()
    db_copy.rollback()
    #print(err)
    #print(type(err))
    #mail(err+type(err))
    file(err)
    
except Exception as msg:
    db_org.rollback()
    db_copy.rollback()
    #print(msg)
    #print(type(msg))
    #mail(msg+type(msg))
    file(msg)
    
except :
    db_org.rollback()
    db_copy.rollback()
    msg="some thing else error occurred"
    #print(msg)
    
    #mail(msg) 
    file(msg)

else:
    #if try block is runned error free
    db_org.commit()
    db_copy.commit()  
    
finally:
    #runs irrrespective of exception
    c_copy.close()
    c_org.close()
    db_org.close()
    db_copy.close()
    
    