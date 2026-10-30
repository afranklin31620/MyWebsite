from smtplib import SMTP
import os , random

def generate_verification_code():
    return random.randint(100_000,999_999)

def send_verification_code(code:int,to_addr:str):
    USER , PASS = os.environ["MAIL_USER"] , os.environ["MAIL_PASS"]
    with SMTP("smtp.gmail.com",587) as mail_server:
        #request features from the server when in unsecured channel
        mail_server.ehlo()
        #once you know the server excepts encryption then you start the tls handshake
        mail_server.starttls()
        #now ask the server for login features
        mail_server.ehlo()
        #login using you credentials
        mail_server.login(USER,PASS)
        #send the message
        mail_server.sendmail(
            from_addr=USER,
            to_addrs=[to_addr],
            msg=f"Hello {to_addr.split("@")[0]}\nYour 6-digit verfication code is {code}"
        )
        print(f"Email sent to {to_addr} successfully!")