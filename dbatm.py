import mysql.connector

class connectdb:
    def __init__(self):
        self.mydb=mysql.connector.connect(host="localhost",database="mydatabase",user='root',password="Mypassword",auth_plugin="mysql_native_password")
                
    def Balance(self,balance):
        sql=f"call Balance('{balance}')"
        mycursor=self.mydb.cursor()
        mycursor.execute(sql)
        self.mydb.commit()
    def withdrawn(self,balance,withdraw_amount):
        sql=f"call withdrawn('{balance}','{withdraw_amount}')"
        mycursor=self.mydb.cursor()
        mycursor.execute(sql)
        self.mydb.commit()
    def deposite(self,balance,deposit_amount):
        sql=f"call Deposite('{balance}','{deposit_amount}')"
        mycursor=self.mydb.cursor()
        mycursor.execute(sql)
        self.mydb.commit()
 