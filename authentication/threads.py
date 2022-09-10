import threading, random
from django.conf import settings
from django.core.mail import send_mail
from django.core.cache import cache


class send_forgot_otp(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    def run(self):
        try:
            otp = random.randint(100001, 999999)
            cache.set(otp, self.email, 350)
            print(otp)
            subject = "OTP to login into your account"
            message = f"The OTP to log in into your email is {otp} \nIts valid only for 2 mins."
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject , message ,email_from ,[self.email])
        except Exception as e:
            print(e)

class send_police_mail(threading.Thread):
    def __init__(self, email, pw):
        self.email = email
        self.pw = pw
        threading.Thread.__init__(self)
    def run(self):
        try:
            subject = "Login Credentials"
            message = f"The login credentails toaccess your account are as following.\n Email : {self.email}\n Password : {self.pw}"
            email_from = settings.EMAIL_HOST_USER
            print("Email ID : " + self.email +  "  Password : " + self.pw)
            send_mail(subject , message ,email_from ,[self.email])
        except Exception as e:
            print(e)


class send_special_email(threading.Thread):
    def __init__(self, sub, body, email_list):
        self.sub = sub
        self.body = body
        self.email_list = email_list
        threading.Thread.__init__(self)
    def run(self):
        try:
            subject = self.sub
            message = self.body
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject , message ,email_from ,self.email_list)
        except Exception as e:
            print(e)