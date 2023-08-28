import smtplib, ssl, os, json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailClient:
    def __init__(self):
        with open('destination_email_addresses.json', 'r') as json_file:
            destination_email_addresses_json = json.load(json_file)

        self.destination_email_addresses = destination_email_addresses_json['destination_email_addresses']
        self.smtp_server_port = os.getenv('SMTP_SERVER_PORT')
        self.smtp_server_domain = os.getenv('SMTP_SERVER_DOMAIN')
        self.source_email_address = os.getenv('SOURCE_EMAIL_ADDRESS')
        self.source_email_password = os.getenv('SOURCE_EMAIL_PASSWORD')

    def send_domain_down_message(self, endpoint, time_downtime_detected):
        message =  MIMEMultipart()
        message['From'] = self.source_email_address
        message['Subject'] = f"Fazool Downtime {endpoint} {time_downtime_detected}"
        message_body = f'The Fazool endpoint {endpoint} is failing health checks as of {time_downtime_detected}'
        message.attach(MIMEText(message_body, 'plain'))

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.smtp_server_domain, self.smtp_server_port, context=context) as smtp_server:
                smtp_server.login(self.source_email_address, self.source_email_password)

                for destination_email_address in self.destination_email_addresses:
                    message['To'] = destination_email_address
                    smtp_server.sendmail(self.source_email_address, destination_email_address, message.as_string())
        except Exception as e:
            print(f"error sending email: {e}")

    def send_domain_back_up_message(self, endpoint, time_downtime_detected, time_domain_back_up):
        message =  MIMEMultipart()
        message['From'] = self.source_email_address
        message['Subject'] = f"Fazool Downtime {endpoint} {time_downtime_detected}"
        message_body = f'The Fazool endpoint {endpoint} is back up. Downtime lasted from {time_downtime_detected} to {time_domain_back_up} for {time_domain_back_up-time_downtime_detected}'
        message.attach(MIMEText(message_body, 'plain'))

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.smtp_server_domain, self.smtp_server_port, context=context) as smtp_server:
                smtp_server.login(self.source_email_address, self.source_email_password)

                for destination_email_address in self.destination_email_addresses:
                    message['To'] = destination_email_address
                    smtp_server.sendmail(self.source_email_address, destination_email_address, message.as_string())
        except Exception as e:
            print(f"error sending email: {e}")