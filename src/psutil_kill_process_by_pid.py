import psutil

proc = psutil.Process(pid=123)
proc.kill()

