# We will need the following module to generate randomized lost packets
import random
import sys
import datetime
from socket import *

serverCache = []
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12001))

while True:
    date = datetime.datetime(2022,12,25)
    Christmas = datetime.datetime(2022,12,25)
    print("Date is ", date)
    rand = random.randint(0, 10)


    message, address = serverSocket.recvfrom(1024)

    if len(serverCache) <10:
        serverCache.append(message)

    if date == Christmas:


        message = message.upper()

        if rand < 4:
            continue
            print("packet not sent")

        # Otherwise, the server responds
        serverSocket.sendto(message, address)
        print("Thank you")
        print(message)
print(serverCache)
