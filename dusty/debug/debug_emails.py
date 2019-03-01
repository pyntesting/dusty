from dusty.drivers.emails import EmailWrapper

smtp_server = "smtp.office365.com"
port = 587  # For starttls
# sender_email = "Auto_EPM-COSR_Mailer@epam.com"
receiver_email = ['karina.taranova@gmail.com', 'Karyna_Taranova@epam.com']
# password = '7j8VE7SrPnBMYrMqqDJLYkUpJ'
sender_email = 'Auto_EPM-MOOC_Reply@epam.com'
password = 'PhTESkpf9#R$q5'

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"

email_client = EmailWrapper(smtp_server=smtp_server, login=sender_email, password=password, port=None)
email_client.send(receiver_email, subject, body)

"""sender_email = Auto_EPM-SSDL_DSAST@epam.com
password = Yc4edG4efjvAgTKThErnS5VJz
Auto_EPM - SSDL_DSAST @ epam.com
SMTP server Name : smtp.office365.com
SMTP port : 587
SSL/TLS : Yes

"""





