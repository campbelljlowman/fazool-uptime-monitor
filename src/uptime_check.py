import requests
import datetime
import email_client as email_client

class UptimeCheck: 
    def __init__(self, endpoint, expected_api_response_message):
        self.email_client = email_client.EmailClient()
        self.endpoint = endpoint
        self.expected_api_response_message = expected_api_response_message
        self.previous_check_is_healthy = True
        self.time_downtime_detected = None

    def check(self):
        current_check_is_healthy = True

        try: 
            response = requests.get(self.endpoint)
            if response.status_code != 200:
                current_check_is_healthy = False
            
            if self.expected_api_response_message != "" and response.text != self.expected_api_response_message:
                current_check_is_healthy = False
        except Exception as e:
            print(f"error executing health check: {e}")
        
        if self.previous_check_is_healthy == True and current_check_is_healthy == False:
            self.time_downtime_detected = datetime.datetime.now()
            print(f"downtime detected for {self.endpoint} at {self.time_downtime_detected}")
            self.email_client.send_domain_down_message(self.endpoint, self.time_downtime_detected)

        if self.previous_check_is_healthy == False and current_check_is_healthy == True:
            recovered_time = datetime.datetime.now()
            print(f"downtime recovered for {self.endpoint} at {recovered_time}")
            self.email_client.send_domain_back_up_message(self.endpoint, self.time_downtime_detected, recovered_time)
            self.time_downtime_detected = None

        self.previous_check_is_healthy = current_check_is_healthy