import socket
import ipaddress


class testPort:

    def __init__(self):


        self.trySocket(self.isPortOpen(21))


    def trySocket(self, port):
        self.port = port

        try:
        
            socket.setdefaulttimeout(10)
            s = socket.socket()
            s.connect(('130.79.128.5', port))
            ans = s.recv(1024)
            print(ans)
        except socket.error as socketerror:
            print("Error: ", socketerror)


    def isPortOpen(self, portStart):
        self.portStart = portStart 

        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        port = self.portStart
        location = ('130.79.128.5', port)
        result_of_check = a_socket.connect_ex(location)
        if result_of_check == 0:
            print("Port: ", port, " is open")
            return port
        else:
            print("Port: ", port, " is closed")
            port += 1
            self.isPortOpen(port)

        a_socket.close()




test = testPort()
