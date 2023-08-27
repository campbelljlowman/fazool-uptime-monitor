import requests
import datetime

class UptimeCheck: 
    def __init__(self, endpoint, expected_api_response_message):
        self.endpoint = endpoint
        self.expected_api_response_message = expected_api_response_message
        self.previous_check_is_healthy = True
        self.time_downtime_detected = None

    def check(self):
        current_check_is_healthy = True

        response = requests.get(self.endpoint)
        if response.status_code != 200:
            current_check_is_healthy = False
        
        if self.expected_api_response_message != "" and response.text != self.expected_api_response_message:
            current_check_is_healthy = False
        
        if self.previous_check_is_healthy == True and current_check_is_healthy == False:
            self.time_downtime_detected = datetime.datetime.now()
            # Send down notification
            pass

        if self.previous_check_is_healthy == False and current_check_is_healthy == True:
            # Send back up message
            pass

        self.previous_check_is_healthy = current_check_is_healthy