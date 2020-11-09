# ETL-Tool
ETL Tool Python and MySql Db (Extract,Transform,Load)

Hello Guys this ETL tool I had made during my internship at " zen Music acadmey ".

This basically a data migrator tools made in python which is used to mantain a dumy/copy database for the above organization.
This is a Cron jobed apllication which was corn jobed at 2:00 am at night means this app runs automatically
everyday 2:00 am if there is some connection error or any runtime error or by any issues the app is unable to do his job the mail would be send to a particular person and a log file is also generated that due to so and so reason(errors) work is unable to complete.

here we also mantain a lookup table which has data that last time when this tool runs successfully and next time whenever this tool will run will sync the dumy database after that particular time till now.

the main file is "migratorTool.py" this file takes his query input from "query.xml" xml file (xml prasing) and runs the query so for large amount of table you just had to add query for in xml file and tool will run for all the tables .

you can use this application from above mentioned file and can see prac files to learn basic things about this tool .There is also a dump sql file which you can import in your mysqldb and you will get dataset for this tool  
