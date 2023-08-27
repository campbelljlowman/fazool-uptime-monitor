import smtplib, ssl, os

class EmailClient:
    def __init__(self):
        self.smtp_server_port = os.getenv('SMTP_SERVER_PORT')
        self.smpt_server_domain = os.getenv('SMPT_SERVER_DOMAIN')
        self.destination_email_address = os.getenv('DESTINATION_EMAIL_ADDRESS')
        self.source_email_address = os.getenv('SOURCE_EMAIL_ADDRESS')
        self.source_email_password = os.getenv('SOURCE_EMAIL_PASSWORD')

    def send_domain_down_message():