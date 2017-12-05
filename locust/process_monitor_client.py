import socket
import pickle


class ProcessMonitorClient(object):

    def __init__(self):
        self.sock = None
        self.charts = {}
        self.connection = False

    def connect_to_agent(self, host='localhost', port=9999):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.connection = True

    def get_carts(self):
        if self.connection:
            self.sock.send('locust client')
            self.charts = pickle.loads(self.sock.recv(1024))
            return self.charts

    def close_connection(self):
        self.sock.send('done')
        self.sock.close()
        self.connection = False


if __name__ == '__main__':
    process_monitor = ProcessMonitorClient()
    print "GET CHARTS ", process_monitor.get_carts()