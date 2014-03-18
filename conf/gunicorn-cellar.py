import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
debug = True
pid = "/srv/cellar/run/logger.pid"
errorlog = "/srv/cellar/logs/error.log"
proc_name = "cellar"
pythonpath = "/srv/cellar/app:/srv/cellar/lib/python2.7:/srv/cellar/scripts:/srv/cellar/lib/python2.7/site-packages"
bind = "unix:/srv/cellar/run/gunicorn.sock"
