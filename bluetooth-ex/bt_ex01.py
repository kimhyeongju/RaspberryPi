from bluetooth import * 

LINE_END =  "\r\n"

# Create the client socket 
client_socket=BluetoothSocket( RFCOMM ) 
client_socket.connect(("00:18:91:D7:A1:D1", 1))  # 접속 

try:
    while True: 
        msg = input("Send : ") + LINE_END 
        client_socket.send(msg) 	# 전송

        msg = client_socket.recv(1024)
        print(f"recived message: {msg}")
        
except KeyboardInterrupt:
    print("Finished")

client_socket.close() 
