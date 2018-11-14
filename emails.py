import smtplib
import email
import email.mime.application

def email():

    gmail_user = 'me@gmail.com'
    gmail_password = 'password'

    sent_from = gmail_user  
    to = ['you@gmail.com']  
    subject = 'title'
    body = "Hey, what's up?\n\n- You"

    email_text = """
    From: %s  
    To: %s  
    Subject: %s

    %s
    """% (sent_from, ", ".join(to), subject, body)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')

email()