import uptime_check
import email_client

SIMPLE_HTTP_UPTIME_CHECK_DOMAINS = ['https://fazool.us']
ENDPOINT_MESSAGE_SPECIFIC_CHECKS = [{'endpoint': 'https://api.fazool.us/hc', 'expected_api_response_message': 'API is healthy!'}]

if __name__ == '__main__':
    print("Setting up checks")
    email_client = email_client.EmailClient()
    
    uptime_checks = []
    for check in SIMPLE_HTTP_UPTIME_CHECK_DOMAINS:
        uptime_checks.append(uptime_check.UptimeCheck(check, ''))

    for check in ENDPOINT_MESSAGE_SPECIFIC_CHECKS:
        uptime_checks.append(uptime_check.UptimeCheck(check['endpoint'], check['expected_api_response_message']))

    for check in uptime_checks:
        check.check()