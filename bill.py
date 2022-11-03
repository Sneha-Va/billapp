import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='hoteldb')
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
    print('')
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
        # #print(f'Total amount {count} ')
        sql = sql="INSERT INTO `billing`( `name`, `phoneno`, `amount`, `date`) VALUES (%s,%s,%s,now())"
        data = (name,phoneno,amount)
        mycursor.execute(sql,data)
        mydb.commit()
        print('data inserted ')
    
    elif(choice==7):
        break