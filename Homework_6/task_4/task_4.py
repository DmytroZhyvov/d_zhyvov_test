import smtplib  # import SMTP (Simple Mail Transfer Protocol)


def sent_email(sender=None, login=None, recipient=None, message=None):
    with smtplib.SMTP('smtp.gmail.com', 587) as smptpObject:
        smptpObject.starttls()
        smptpObject.login(sender, login)
        smptpObject.sendmail(sender, recipient, message)



