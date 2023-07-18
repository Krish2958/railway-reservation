import mysql.connector
import random

# Establishing the database connection
mycon = mysql.connector.connect(host='localhost', user='root', passwd='Your_Password')
if mycon.is_connected():
    print("-" * 170)
    print("Successfully Connected...")
    print("-" * 170)

# Creating necessary tables and database
cursor = mycon.cursor()
mycon.autocommit = True
s1 = "create database railway"
cursor.execute(s1)

s1 = "USE railway"
cursor.execute(s1)

s1 = "create table railway (name varchar(100), phno varchar(15), tc_now varchar(20) primary key, age int(5), gender varchar(50), from_f varchar(100), to_t varchar(100), date_d varchar(20))"
cursor.execute(s1)

s1 = "create table user_accounts(fname varchar(100), lname varchar(100), user_name varchar(100), password varchar(100) primary key, phno varchar(15), gender varchar(50), dob varchar(50), age varchar(4))"
cursor.execute(s1)

# FILE NAME: MAIN

# Function for user sign-in
def SIGN_IN():
    import mysql.connector
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='Your_Password', database='Railway')
    cursor = mycon.cursor()
    mycon.autocommit = True
    a = input('USER NAME:')
    b = input('PASS WORD:')
    try:
        s1 = "SELECT user_name FROM user_accounts WHERE password='{}'".format(b)
        c1 = "SELECT fname, lname FROM user_accounts WHERE password='{}'".format(b)
        cursor.execute(c1)
        data1 = cursor.fetchall()[0]
        data1 = list(data1)
        data1 = data1[0] + ' ' + data1[1]
        cursor.execute(s1)
        data = cursor.fetchall()[0]
        data = list(data)[0]
        if data == a:
            print(' HELLO ', data1)
            return True
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')


# Function for user sign-up
def SIGN_UP():
    import mysql.connector
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='Your_Password', database='Railway')
    cursor = mycon.cursor()
    mycon.autocommit = True
    f = input("FIRST NAME:")
    l = input("LAST NAME:")

    a = input('USER NAME:')
    b = input('PASS WORD:')
    c = input('RE-ENTER YOUR PASS WORD:')
    ph = int(input("PHONE NUMBER:"))
    print(' M=MALE', '\n', 'F=FEMALE', '\n', 'N=NOT TO MENTION')
    gen = input('ENTER YOUR GENDER:')
    print("ENTER YOUR DATE OF BIRTH")
    d = input("DD:")
    o = input("MM:")
    p = input("YYYY:")
    dob = d + '/' + o + '/' + p
    age = int(input('ENTER YOUR AGE:'))
    v = {'m': 'MALE', 'f': 'FEMALE', 'n': 'NOT TO MENTION'}
    if b == c:
        try:
            c1 = "INSERT INTO user_accounts values('{}','{}','{}','{}',{},'{}','{}',{})".format(f, l, a, b, ph, v[gen], dob, age)
            cursor.execute(c1)
            print('WELCOME', f, l)
            return True
        except:
            print("PASSWORD ALREADY EXISTS")
            return False
    else:
        print('BOTH PASSWORDS ARE NOT MATCHING')


# Function to delete the user account
def DELETE():
    import mysql.connector
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='Your_Password', database='Railway')
    cursor = mycon.cursor()
    mycon.autocommit = True
    a = input('USER NAME:')
    b = input('PASS WORD:')
    try:
        s1 = "SELECT user_name FROM user_accounts WHERE password='{}'".format(b)
        cursor.execute(s1)
        data = cursor.fetchall()[0]
        data = list(data)
        if data[0] == a:
            print('YOUR ACCOUNT DETAILS ARE: ')
            s1 = "SELECT user_name FROM user_accounts WHERE password='{}'".format(b)
            c1 = "SELECT fname, lname FROM user_accounts WHERE password='{}'".format(b)
            cursor.execute(c1)
            data1 = cursor.fetchall()[0]
            data1 = list(data1)
            data1 = data1[0] + ' ' + data1[1]
            cursor.execute(s1)
            data = cursor.fetchall()[0]
            data = list(data)
            if data[0] == a:
                x = ['FIRST NAME', 'LAST NAME', 'PHONE NUMBER', 'GENDER', 'DATE OF BIRTH', 'AGE']
                s1 = "SELECT fname, lname, phno, gender, dob, age FROM user_accounts WHERE password='{}'".format(b)
                cursor.execute(s1)
                data = cursor.fetchall()[0]
                data = list(data)
                print("\t\t\t\t\t\t\t", x[0], ':::', data[0])
                print("\t\t\t\t\t\t\t", x[1], ':::', data[1])
                print("\t\t\t\t\t\t\t", x[2], ':::', data[2])
                print("\t\t\t\t\t\t\t", x[3], ':::', data[3])
                print("\t\t\t\t\t\t\t", x[4], ':::', data[4])
                print("\t\t\t\t\t\t\t", x[5], ':::', data[5])
                print(' 1.YES  TO PROCEED')
                print(' 2.NO   TO CANCEL')
                vi = int(input('Enter Your Choice:  (1/2)'))
                if vi == 1:
                    b1 = "DELETE FROM user_accounts WHERE password = '{}'".format(b)
                    cursor.execute(b1)
                    return True
                elif vi == 2:
                    print('THANK YOU')
                else:
                    print('ERROR 404: PAGE NOT FOUND')
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')


# Function to view user account details
def ACCOUNT():
    import mysql.connector
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='Your_Password', database='Railway')
    cursor = mycon.cursor()
    mycon.autocommit = True
    a = input('USER NAME:')
    b = input('PASS WORD:')
    try:
        s1 = "SELECT user_name FROM user_accounts WHERE password='{}'".format(b)
        c1 = "SELECT fname, lname FROM user_accounts WHERE password='{}'".format(b)
        cursor.execute(c1)
        data1 = cursor.fetchall()[0]
        data1 = list(data1)
        data1 = data1[0] + ' ' + data1[1]
        cursor.execute(s1)
        data = cursor.fetchall()[0]
        data = list(data)
        if data[0] == a:
            x = ['FIRST NAME', 'LAST NAME', 'PHONE NUMBER', 'GENDER', 'DATE OF BIRTH', 'AGE']
            s1 = "SELECT fname, lname, phno, gender, dob, age FROM user_accounts WHERE password='{}'".format(b)
            cursor.execute(s1)
            data = cursor.fetchall()[0]
            data = list(data)
            print(x[0], ':::', data[0])
            print(x[1], ':::', data[1])
            print(x[2], ':::', data[2])
            print(x[3], ':::', data[3])
            print(x[4], ':::', data[4])
            print(x[5], ':::', data[5])
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')


b = []


# Function to generate a unique ticket number
def tc_no():
    d = random.randint(10000000, 99999999)
    for a in range(1):
        if d not in b:
            b.append(d)
            global tn
            tn = b.pop()


def menu():
    while True:
        print("WELCOME TO ONLINE RAILWAY RESERVATION SYSTEM")
        print('1.SIGN IN')
        print('2.SIGN UP')
        print('3.DELETE ACCOUNT')
        print('4.EXIT')
        ch1 = int(input("Enter Your Choice"))
        if ch1 == 1:
            a = SIGN_IN()
            if a:
                print("WELCOME")
                main()

        elif ch1 == 2:
            a = SIGN_UP()
            if a:
                main()
            else:
                print("PASSWORD ALREADY EXISTS")

        elif ch1 == 3:
            c = DELETE()
            if c:
                print("Account DELETED")
            else:
                print("YOUR PASSWORD OR USERNAME IS INCORRECT")

        elif ch1 == 4:
            print("Thank You For Visiting")
            break

        else:
            print("Error 404 : PAGE NOT FOUND")


def Ticket_Booking():
    import mysql.connector
    Mycon = mysql.connector.connect(host='localhost', user='root', passwd='Your_Password', database='Railway')
    Cursor = mycon.cursor()
    mycon.autocommit = True
    nm = input('Enter Your Name:')
    phno = input('Enter Your Phone Number:')
    age = int(input('Enter Your Age:'))
    print(' M=MALE', '\n', 'F=FEMALE', '\n', 'N=NOT TO MENTION')
    gender = input('Enter Your Gender:')
    Gender = gender.upper()
    fr = input('Enter Your Starting Station:')
    to = input('Enter Your Destination Station:')
    date1 = input('Enter Date(dd):')
    date2 = input('Enter Month(mm):')
    date3 = input('Enter Year(yyyy):')
    date = date1 + "/" + date2 + "/" + date3
    a = {'M': 'MALE', 'F': 'FEMALE', 'N': 'NOT TO MENTION'}
    v = a[Gender]
    tc_no()

    s1 = "insert into railway values ('{}',{},{},{},'{}','{}','{}','{}')".format(nm, phno, tn, age, v, fr, to, date)

    cursor.execute(s1)
    print('BOOKED SUCCESSFULLY')
    print("YOUR TICKET NO. IS :  ", tn)
    print("DO YOU WANT TO PRINT YOUR TICKET:")
    print("1.YES")
    print("2. NO")
    ch2 = int(input("ENTER YOUR CHOICE :"))
    if ch2 == 1:
        tn1 = int(input('enter your ticket number:'))
        try:
            s1 = "select * from railway where tc_now={}".format(tn1)
            cursor.execute(s1)
            data = cursor.fetchall()[0]
            Data = list(data)
            a = ['NAME', 'PHONE,NUMBER', 'TICKET NUMBER', 'AGE', 'GENDER', 'STARTING POINT', 'DESTINATION', 'DATE', ]
            print(a[0], '::::', Data[0].upper())
            print(a[1], '::::', Data[1])
            print(a[2], '::::', Data[2])
            print(a[3], '::::', Data[3])
            print(a[4], '::::', Data[4].upper())
            print(a[5], '::::', Data[5].upper())
            print(a[6], '::::', Data[6].upper())
            print(a[7], '::::', Data[7])
        except:
            print("TICKET DOES NOT EXISTS")
    elif ch2 == 2:
        print('THANK YOU')
    else:
        print('ERROR 404: PAGE NOT FOUND')


def Ticket_Checking():
    import mysql.connector
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='Your_Password', database='Railway')
    cursor = mycon.cursor()
    mycon.autocommit = True
    tn1 = int(input('enter your ticket number:'))
    try:
        s1 = "select * from railway where tc_now={}".format(tn1)
        cursor.execute(s1)
        data = cursor.fetchall()[0]
        Data = list(data)
        a = ['NAME', 'PHONE,NUMBER', 'TICKET NUMBER', 'AGE', 'GENDER', 'STARTING POINT', 'DESTINATION', 'DATE', ]
        print(a[0], '::::', Data[0].upper())
        print(a[1], '::::', Data[1])
        print(a[2], '::::', Data[2])
        print(a[3], '::::', Data[3])
        print(a[4], '::::', Data[4].upper())
        print(a[5], '::::', Data[5].upper())
        print(a[6], '::::', Data[6].upper())
        print(a[7], '::::', Data[7].upper())
    except:
        print("TICKET DOES NOT EXISTS")


def Ticket_Cancelling():
    import mysql.connector
    mycon = mysql.connector.connect(host='localhost', user='root', passwd='Your_Password', database='railway')
    cursor = mycon.cursor()
    mycon.autocommit = True
    tcno = input('Enter Your Ticket Number:')
    s1 = "delete from railway where tc_now={}".format(tcno)
    cursor.execute(s1)
    print('TICKET CANCELLED')


def main():
    while True:
        print("\n", '1.TICKET BOOKING', "\n", '2.TICKET CHECKING', "\n", '3.TICKET CANCELLING', "\n", '4.ACCOUNT DETAILS',
              "\n", '5.LOG OUT')
        ch = int(input('Enter Your Choice:'))
        if ch == 1:
            Ticket_Booking()
        elif ch == 2:
            Ticket_Checking()
        elif ch == 3:
            Ticket_Cancelling()
        elif ch == 4:
            Account()
        elif ch == 5:
            print('THANK YOU')
            print("*" * 179)
            break
        else:
            print('ERROR 404: ERROR PAGE NOT FOUND')


menu()

