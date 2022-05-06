import socket
import sys
import time
from socket import *

pings = 1
packet = ["candy", "chocolate", "ps4", "hat", "toffee","flower","tea","sweet","custard","toy","ring"]
#Send ping 10 times
while pings < 11:

    #Create a UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    #Set a timeout value of 1 second
    clientSocket.settimeout(1)

    #Ping to server
    message = (packet[pings]).encode("utf-8")

    addr = ("127.0.0.1", 12001)

    #Send ping
    start = time.time()
    clientSocket.sendto(message, addr)

    #If data is received back from server, print
    try:
        data, server = clientSocket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print (data, " " , pings ," ", elapsed)

    #If data is not received back from server, print it has timed out
    except timeout:
        print ('REQUEST TIMED OUT')

    pings = pings + 1
