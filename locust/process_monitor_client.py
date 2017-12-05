import socket
import pickle
from multiprocessing import Process


class ProcessMonitorClient(object):

    def __init__(self, host='localhost', port=9999):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.charts = {}

    def get_carts(self):
        self.sock.send('locust client')
        self.charts = pickle.loads(self.sock.recv(1024))
        return self.charts

    def close_connection(self):
        self.sock.send('done')
        self.sock.close()


if __name__ == '__main__':
    process_monitor = ProcessMonitorClient()
    print "GET CHARTS ", process_monitor.get_carts()