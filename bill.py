import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='hoteldb')
mycursor = mydb.cursor()
total=0
item=[]
while(True):
    print("select the option")
    print("1.tea.....20")
    print('2. juice....70')
    print('3.coffee....15')
    print('4.dosa....25')
    print('5.biriyani...140')
    print('6. generate bill')
    print('7.exit')
    choice=int(input("enter the choice"))
    if(choice==1):
        print("added tea")
        qty=int(input("enter the quandity"))
        total=20*qty
        item.append("tea x"+str(qty))
    elif(choice==2):
        print("juice added")
    elif(choice==3):
        print("coffee added")
    elif(choice==4):
        print("dosa added")
    elif(choice==5):
        print("biriyani added")
    elif(choice==6):
        print("gnerate bill")
    elif(choice==7):
        break