import mysql.connector
import sys 
from tabulate import tabulate
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='hoteldb')
except mysql.connector.Error as e:
    sys.exit("connection error")
mycursor = mydb.cursor()
total=0
item=[]
l=[]
while(True):
    print("select the option")
    print("1.tea.....20")
    print('2. juice....70')
    print('3.coffee....15')
    print('4.dosa....25')
    print('5.biriyani...140')
    print('6. generate bill')
    print('7.view all transaction')
    print('8.day wise transcation')
    print('9.transaction summary')
    print('10. exit')
    choice=int(input("enter the choice"))
    if(choice==1):
        print("added tea")
        qty=int(input("enter the quandity"))
        total=20*qty
        l.append("tea x"+str(qty))
        print("quantity=",qty)
        print("total=",total)
    elif(choice==2):
        print("juice added")
        qty=int(input("enter the quandity"))
        total=20*qty
        item.append("juice x"+str(qty))
        print("quantity=",qty)
        print("total=",total)
    elif(choice==3):
        print("coffee added")
        qty=int(input("enter the quandity"))
        total=20*qty
        l.append("coffee x"+str(qty))
        print("quantity=",qty)
        print("total=",total)
    elif(choice==4):
        print("dosa added")
        qty=int(input("enter the quandity"))
        total=20*qty
        l.append("dosa x"+str(qty))
        print("quantity=",qty)
        print("total=",total)
    elif(choice==5):
        print("biriyani added")
        qty=int(input("enter the quandity"))
        total=20*qty
        l.append("juice x"+str(qty))
        print("quantity=",qty)
        print("total=",total)
    elif(choice == 6):
        print('You enter into billing section')
        name = input('Enter the name : ')
        phoneno = input('Enter the phone number : ')
        #dates = input('Enter the date in the form of yyyy-mm-d : ')
        l1 = []
        l1.extend(l)
        count = 0
        for i in l1:
            l.remove(i)
            amount = count
         #print(f'Total amount {count} ')
        try:
            sql = sql="INSERT INTO `billing`( `name`, `phoneno`, `amount`, `date`) VALUES (%s,%s,%s,now())"
            data = (name,phoneno,amount)
            mycursor.execute(sql,data)
            mydb.commit()
        except mysql.connector.Error as e:
            sys.exit("connection error")
        print('data inserted ')
    elif(choice==7):
        print("view all transaction")
        date=input("enter the date(yyyy-mm-d)")
        try:
            sql="SELECT `id`, `name`, `phoneno`, `amount`, `date` FROM `billing`  WHERE `date`='"+date+"'"
            mycursor.execute(sql)
            result=mycursor.fetchall()
            print(tabulate(result,headers=["name","phoneno","amount",date],tablefmt="psql"))
        except mysql.connector.Error as e:
            sys.exit("connection error")
        print(result)
    elif(choice==8):
        print("day wise transcation")
        date=input("enter the date(yyyy-mm-d)")
        try:
            sql="SELECT SUM(`amount`) FROM `billing` WHERE `date`='"+date+"'"
            mycursor.execute(sql)
            result=mycursor.fetchall()
            print(tabulate(result,headers=["date"],tablefmt="psql"))
        except mysql.connector.Error as e:
            sys.exit("connection error")
        print(result)
        print(result)
    elif(choice==9):
        print("transaction summary")
        date1=input("enter date")
        date2=input("enter date")
        try:
            sql="SELECT SUM(`amount`) FROM `billing` WHERE `date` BETWEEN '"+date1+"' AND '"+date2+"'"
            mycursor.execute(sql)
            result=mycursor.fetchall()
            print(tabulate(result,headers=["date1","date2"],tablefmt="psql"))
        except mysql.connector.Error as e:
            sys.exit("transcation  error")
        print(result)
        
    
    elif(choice==10):
        break