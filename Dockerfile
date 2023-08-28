FROM python:3.11
LABEL org.opencontainers.image.source=https://github.com/campbelljlowman/fazool-uptime-monitor

WORKDIR /app

COPY *.py /app/

COPY requirements.txt /app/
RUN pip install -r requirements.txt

CMD ["python3", "-u", "uptime_monitor.py"]