import uptime_check as uptime_check
import time, os

SIMPLE_HTTP_UPTIME_CHECK_DOMAINS = ['https://fazool.us']
ENDPOINT_MESSAGE_SPECIFIC_CHECKS = [{'endpoint': 'https://api.fazool.us/hc', 'expected_api_response_message': 'API is healthy!'}]
INPUT_UPTIME_CHECK_INTERVAL_SECONDS = os.getenv('UPTIME_CHECK_INTERVAL_SECONDS')
UPTIME_CHECK_INTERVAL_SECONDS = int(INPUT_UPTIME_CHECK_INTERVAL_SECONDS) if INPUT_UPTIME_CHECK_INTERVAL_SECONDS and INPUT_UPTIME_CHECK_INTERVAL_SECONDS.isdigit() and int(INPUT_UPTIME_CHECK_INTERVAL_SECONDS) >= 15 else 30

if __name__ == '__main__':
    uptime_checks = []
    for check in SIMPLE_HTTP_UPTIME_CHECK_DOMAINS:
        uptime_checks.append(uptime_check.UptimeCheck(check, ''))

    for check in ENDPOINT_MESSAGE_SPECIFIC_CHECKS:
        uptime_checks.append(uptime_check.UptimeCheck(check['endpoint'], check['expected_api_response_message']))

    while True:
        print("executing health checks")
        for check in uptime_checks:
            check.check()

        time.sleep(UPTIME_CHECK_INTERVAL_SECONDS)