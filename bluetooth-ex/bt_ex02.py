from bluetooth import *
from btsocket import BtSocket

LINE_END = "\r\n"

# client_socket=BluetoothSocket(RFCOMM)
client_socket = BtSocket( RFCOMM )
client_socket.connect(("00:18:91:D7:A1:D1", 1))

try:
    while True: 
        msg = input("Send : ") + LINE_END 
        client_socket.send(msg) 	# 전송

        # msg = client_socket.recv(1024)
        msg = client_socket.readline()
        print(f"recived message: {msg}")
        
except KeyboardInterrupt:
    print("Finished")

client_socket.close() 