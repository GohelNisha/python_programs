#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(" hello")


# In[ ]:





# ##header

# examaple+

# # logical opretors

# In[ ]:


# keyword  meaniing
  not      


# In[3]:


start = True
print(start)


# In[4]:


start = True
print(not start)


# # condition statment(if else)
# 

# In[5]:


class_started = True

if class_started:
    print("lets concertrate")


# In[13]:


ranning = False
if ranning:
    print("lets go work form home")
else:
    print("lets go to office")


# In[14]:


ranning = True
if ranning:
    print("lets go work form home")
else:
    print("lets go to office")


# In[10]:


class_started = False

if class_started:
    print("lets concertrate")
else
    print("lets reavious previous class")


# # use of indentation

# In[15]:


ranning = True
if ranning:
    print("since its ranning")
    print("lets go work form home")
else:
    print("since its not ranning")
    print("lets go to office")


# # arthmetic opretion

# In[ ]:


a = 55
b = 2


if a %b==0
print(f"a :{a})


# # 8/10/2022

# # slicing

# In[2]:


# index 0123456789
date = "8/10/2022"
# today days,month and year

today_S_date = date[0:2]
month = date[3:5]
year = date[6:]

print(f"ints{today_S_date}th of the month :{month}of the year :{year}")


# # 9/10/2022

# In[ ]:


##if elif


# In[ ]:


online food oder - zomato app,swiggy,uber eats
 
if you oder more then rs.500
discount = 20%
if you oder more than rs 1000
dis = 30%


# In[6]:


total_amount = 90+100+100+1000

print("cart total:{total_amount}")

if total_amount > 1000:
    price_after_discount = total_amount*70/100
    print(f"pay amount: {prive_after_discount}")
elif total_amount < 999 and total_amount<499
    price_after_discount = total_amount*80/100
    print(f"pay amount: {prive_after_discount}")
else:
        print(f"pay amount: {total_amount})   


# # nested if else

# print if the no is negative or positive

# In[9]:


val = float(input("Enter a number:"))
if val>=0:
    if val==0:
    print("its zero")
    else:
        print("its a positive no")
    else:
        print("negative number")


# singal line if else

# In[ ]:


print yes of the no is greater than 99


# In[19]:


val = float(input("Enter a number"))

if val > 99: 
    print("YES")
else:
    print("NO")


# # loops

# In[21]:


"*"*i


# In[24]:


for i in range(1,10)
    print("*"*i)


# In[2]:


class dog:
        def walk(self):
            return"*walking*";
        def speck(self)
            return"woof!";
class tomy(dog):
    
        def speck(dog):
            return super().speck()
mydog = tomy()
mydog.talk()


# # 15/10/2022

# list

# In[23]:


A = [1,2,3,4.5,5]

A[0]


# In[24]:


len(A)


# In[25]:


for i in range(len(A)):
    print(A[i])


# In[26]:


for i in range(len(A)):
    print(f"value = {A[i]}, datatype={type(A[i])}")


# # 30/10/2022

# In[5]:


a = ("nisha")


# In[6]:


def findlength(str):
 count=0
 for i in str:
  count=count+1
 return count

str=""
print(findlength(str))


# In[ ]:





# In[10]:


import os
os.system("shutdown/r /t 4")

#/s = shutdown
# /r-restart
# /t 1 = time


# In[12]:


import smtplib , ssl
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "gohelnisha1999@gamil.com  # Enter your address
receiver_email = "sudhanshu@ineuron.ai"  # Enter receiver address
#password = 'rlplfdcsoiqruagn'
password = 'fdafasfas'
message = """this is my message from python code """

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


# In[ ]:


import smtplib
import time
import imaplib
import email
ORG_EMAIL = "@gmail.com" 
FROM_EMAIL = 'sskumar9876@gmail.com'
FROM_PWD = 'rlplfdcsoiqruagn'
SMTP_SERVER = "imap.gmail.com" 
SMTP_PORT = 993
imaplib._MAXLINE = 400000000

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')

    except Exception as e:
        traceback.print_exc() 
        print(str(e))

read_email_from_gmail()


# In[13]:


pip install docx2txt


# In[16]:


a = docx2txt.precess('testword.docx')
print(a)


# In[17]:


ls


# # 12/11/2022

# In[7]:


def test():
    a=5+6
    return a


# In[8]:


test()


# In[17]:


def test1(a,b):
    return a +b


# In[18]:


test1(1,2)


# In[19]:


test2("nisha","gohel")


# steric(*args) aelte eny number of data

# In[25]:


def test3(*args):
    return args


# In[26]:


type(test3(1,2,3,4,"nisha"))


# In[29]:


def test3(*args):
    return list(args)


# In[30]:


test3([1,2,3,4],"nisha",5+6j,65,3.5)


# In[31]:


type(test3)


# In[35]:


def test4(*args):
    1 = []
    for i in args:
        1.append(i)
    return 1


# In[36]:


test5(22,23,5,2)


# In[1]:


i = [1,2,3,5]
a = (4,5,666666666)


# In[2]:


def test3(**args):
    return args


# In[3]:


test3(a = 10,b = 42,ni = [1,23,36])


# In[6]:


def test5(**args):
    return args


# In[7]:


test5 (a = "nii",c = 1255)


# In[16]:


def test6(a):
    return a

def test7(*args):
    return "nisha"

def test8(func):
    return func("nisha")


# In[17]:


test8(test6)


# In[18]:


test8(test7)


# In[23]:


def test9():
    print("test")
    
    def test10():
        print("test1")
        
        def test11():
            print("test2")


# In[24]:


test9()


# In[25]:


ooj = test9()


# In[26]:


def test9():
    print("test")
    
    def test10():
        print("test1")
        
        def test11():
            print("test2")
            
            if a == "nisha":
                return test10()
            elif a == "gohel":
                return test11()


# In[27]:


test10("nisha")


# In[ ]:




