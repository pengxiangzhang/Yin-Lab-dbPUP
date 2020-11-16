workers = 5

threads = 2

bind = '0.0.0.0:8888'

worker_class = 'gevent'

worker_connections = 2000

pidfile = '/home/bo/BiologyLabWeb.pid'

accesslog = '/home/bo/BiologyLabWeb_access.log'

errorlog = '/home/bo/BiologyLabWeb_error.log'

loglevel = 'warning'

reload = True
