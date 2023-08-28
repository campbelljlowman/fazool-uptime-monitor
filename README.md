# fazool-uptime-monitor
Uptime monitor for fazool production domains

Runs certain checks on public APIs on a regular interval and sends alerts if the results are unexpected

# Environment variables
SMTP_SERVER_PORT=
SMTP_SERVER_DOMAIN=
SOURCE_EMAIL_ADDRESS=
SOURCE_EMAIL_PASSWORD=
UPTIME_CHECK_INTERVAL_SECONDS= (must be greater than 15 seconds, defaults to 30)