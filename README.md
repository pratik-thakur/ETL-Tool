# ETL-Tool
ETL Tool Python and MySql Db (Extract, Transform, Load)

Hello, Guys this ETL tool I had made during my internship at " Zen Music Academy ".

This is a data migrator tool made in python which is used to maintain a dummy/copy database for the above organization.

This is a Cron jobed application that was corn jobed at 2:00 am means this app runs automatically every day at 2:00 am. if there is some connection error or any runtime error or by any issues, the app is unable to do his job the mail would be sent to a particular person and a log file is also generated that due to so and so reason(errors) work is unable to complete.

Here in this application we also maintain a lookup table which has data that last time when this tool runs successfully and next time whenever this tool will run will sync the dummy database after that particular time till now.

the main file is "migratorTool.py" this file takes his query input from the "query.xml" XML file (XML parsing) and runs the query so for a large number of the table you just had to add a query for that table in XML file and tool will run for all the tables.

you can use this application from the above-mentioned file and can see prac files to learn basic things about this tool. There is also a dump SQL file which you can import in your MySQL DB and you will get a dataset for this tool  

For any suggestion/improvement in this, you are most welcome, just send me a pull request
