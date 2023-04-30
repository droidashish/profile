
# wsgi_app = "mysite.wsgi:application"
command = '/home/ashish/.local/bin/gunicorn'
pythonpath = '/usr/bin/python3'
bind = '192.168.29.148:8000'
workers = 3
# Restart workers when code changes (development only!)
reload = True
# Write access and error info to /var/log
# accesslog = errorlog = "/var/log/gunicorn/dev.log"
# Redirect stdout/stderr to log file
capture_output = True
