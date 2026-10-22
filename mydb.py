# download mysql
# install mysql connector
# install mysql
# 


import mysql.connector
dataBase = mysql.connector.connect(
    'host':'localhost',
    'user':'root',
    'password':'QWer!@34',
)

cursorObject=dataBase.cursor()
cursorObject.execute("django_crm_db")
print("All Done!")

