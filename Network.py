import socket
import sys
import threading

class Network(object):

    crossFound = False
    crossAzi = None
    rectFound = False
    rectAzi = None
    portNumber = 0
    isInitialized = False
    connection = None


    class myThread (threading.Thread):
        network = None
        def __init__(self, threadID, name, counter, network):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter
            self.network = network

        def run(self):
            print ("Starting " + self.name)
            Network.startServer(self.network)
            print ("Exiting " + self.name)

    def setCross(self):
        self.crossFound = False
        self.crossAzi = None

    def setCrossAzi(self, azi):
        self.crossFound = True
        self.crossAzi = azi

    def setRect(self):
        self.rectFound = False
        self.rectAzi = None

    def setRectAzi(self, azi):
        self.rectFound = True
        self.rectAzi = azi

    def waitForPing(self): #wait for something to be sent
        if(s != None):
            receive = s.recv(1024)
            if receive == None or receive == ' ' :
                print ("Hasn't received ping")

    def sendMessage(self, message): # send message to NTable client
        if(isInitialized !=  False):
            connection.send(message + b'\n')

    def __init__(self):
        global s
        s = None
        global portNumber
        portNumber = 3341
        global isInitialized
        isInitialized = False

    def userServer(self):
        thread1 = self.myThread(1, "Thread-1", 1, self)
        thread1.start()
        print("thread started")

    def startServer(self): #startServer
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "localhost"
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, portNumber))

        global connection
        print ("in startServer")
        s.listen(5)
        #while True:

        connection, addr = s.accept()
        print ("accepted" + str(addr))
        global isInitialized
        isInitialized = True

        while True:
            if(self.crossFound != None):
                self.sendMessage(b"crossFound: " + str(self.crossFound).encode('utf-8'))
                self.crossFound = None
            if(self.crossAzi != None):
                self.sendMessage(b"crossAzi: " + str(self.crossAzi).encode('utf-8'))
                self.crossAzi = None
            if(self.rectFound != None):
                self.sendMessage(b"rectFound: " + str(self.rectFound).encode('utf-8'))
                self.rectFound = None
            if(self.rectAzi != None):
                self.sendMessage(b"rectAzi: " + str(self.rectAzi).encode('utf-8'))
                self.rectAzi = None
