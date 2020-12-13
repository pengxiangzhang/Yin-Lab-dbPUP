#Services
workers = 4
threads = 2
worker_class = 'gevent'
daemon = 'false'
bind = '0.0.0.0:8888'
x_forwarded_for_header = 'X-FORWARDED-FOR'
worker_connections = 1000

#Log
pidfile = '/home/bo/BiologyLabWeb.pid'
accesslog = '/home/bo/BiologyLabWeb_access.log'
errorlog = '/home/bo/BiologyLabWeb_error.log'
loglevel = 'debug'

#Development
reload = True
