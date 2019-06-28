import socket
from queue import Queue
import threading
import log

log.init_log('scanport')

q = Queue()
print_lock = threading.Lock()

server="127.0.0.1"

### méthode : fonction
def scanport(port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connect = s.connect((server, port))         
        with print_lock:
            print('Port', port, 'is open!')
            connect.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        scanport(worker)
        q.task_done()
    
    
for x in range(200):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()
        
for worker in range(1, 500):
    q.put(worker)

q.join()
