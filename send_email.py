import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
def send_email(receiver,sub,genrated_body):
    smtp_server = 'smtp.gmail.com'
    s = smtplib.SMTP('smtp.gmail.com',port=587)
    s.starttls()
    subject = sub
    body = genrated_body
    message = f'Subject: {subject} \n\n {body}'
    s.login(os.environ.get('email'),password=os.environ.get('pass'))
    print('login successfull')

    s.sendmail(from_addr=os.environ.get('email'),to_addrs=receiver,msg=message)
    print('message sent successfull')
    s.quit()
def mail_split(r_mail,script):
    parts = script.split('Body:')
    subject=parts[0].replace('Subject: ','').strip()
    body = parts[1].strip()
    send_email(r_mail,sub=subject,genrated_body=body)

email_tool_schema = {
    'type': 'function',
    'function': {
        'name':'send_email',
        'description':'send a professional email with a subject and body and search on the internet for that company email on a internet when not the user provide the email',
        'parameters':{
            'type':'object',
            'properties':{
            'receiver_email':{'type':'string'},
            'subject':{'type':'string'},
            'body':{'type':'string'},
            },
        
        'required':['receiver_email','subject','body']
    }
    }
}