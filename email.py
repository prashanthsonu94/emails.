# -random letter generator-
# import string
# var1 = string. ascii_letters

# import random
# var2 = random. choice(string. ascii_letters)
# print(var2)

# import string
# var1 = string. ascii_letters

# import random
# var2 = random. choice(string. ascii_letters)
# print(var2)

# import uuid  
# # Printing random id using uuid1()  
# print ("The random generated uuid is : ", uuid.uuid1())  

# import random

# a1=random.randint(1,9999)
# print(a1)

# import uuid


# r1=str(uuid.uuid4().int>>64)[0:16]
# r2=str(uuid.uuid4().int>>64)[0:16]
# r1=str(uuid.uuid1().int>>64)[0:16]

# print("id:",r1,r2)

# data_status={"responsestatus":0,"result":""}

# import random
# data_status={"responsestatus":0,"result":""}
# def uniqueid():
#     digit16 = random.getrandbits(64)
#     data_status["responsestatus"]=1
#     data_status["result"]=digit16
#     return data_status
# r1=uniqueid()
# def otheruniqueid():
#     digit8 = random.getrandbits(32)
#     data_status["result"]=digit8
#     return data_status
# r2=otheruniqueid()
# print(r1)
# # print(r2)

# from django.utils.crypto import get_random_string
# import random
# data_status={"responsestatus":0,"result":""}

# def generate_account_id():
#     # return get_random_string(16, allowed_chars='0123456789')
#     return random.getrandbits(64)
# r1=generate_account_id()
# print(r1)


# import secrets
# hexstr = secrets.token_hex(8)
# your_id = int(hexstr, 16)
# print(hexstr)
# print(your_id)




# import random
  
# # 5 random number with 4 bits
# for i in range(4):
#     print(random.getrandbits(64))






# def fun1(name):
#     return name.upper()
# print(fun1("prashanth"))




# def fun1(*args):
#     print(args)
# fun1("Prashanth","ram","sai")


# import smtplib
  
# # list of email_id to send the mail
# li = ["prashanthsonu94@gmail.com"]
  

# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.starttls()
# password=input("enter your password:")
# s.login("prashanthsonu94@gmail.com",password)
# SUBJECT = "Hello"
# message = "Hi,Hello"
# s.sendmail("prashanthsonu94@gmail.com",li,message)

# s.quit()
# msg="Message sent"
# print(msg)


# import smtplib

# # SERVER = <localhost>

# FROM = "prashanthsonu94@gmail.com"
# TO = "prashanthsonu94@gmail.com"

# SUBJECT = "Hello!"

# message = "Test"

# TEXT = "This message was sent with Python's smtplib."
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# password = input("Enter your password:")
# server.login(FROM,password)
# server.sendmail(FROM, TO, message)
# server.quit()
# msg="Mail sent"
# print(msg)




import smtplib

sender = 'prashanthsonu94@gmail.com'
receivers = 'sai.kerla@apptrinity.com'

message = """From:<prashanthsonu94@gmail.com>
To:<gollaswathi078@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message through python.
"""

try:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    password = input("Enter your password:")
    server.login(sender,password)
    server.sendmail(sender, receivers, message)         
    print ("Successfully sent email")
except Exception as e:
    print("Unable to send mail")