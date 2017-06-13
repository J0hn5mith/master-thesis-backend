import smtplib

EMAIL_HOST = 'avior.uberspace.de'
EMAIL_HOST_USER = 'develop@jan-meier.ch'
EMAIL_HOST_PASSWORD = 'x;W*$XUp&sD=6Dg6wFL87u46}mRz9Tx3N>Z$NDbVB4w$Hk9o?o'
EMAIL_PORT = 587

try:
    smtp = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    smtp.sendmail('test@jan-meier.ch', 'test@jan-meier.ch', 'Hello smtp')
except smtplib.SMTPException as e:
    print("Error: unable to send email")
    print(e)
