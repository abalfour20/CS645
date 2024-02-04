import socket
import threading

#This code will act as the server. 
#The server will handle receiving information fron a client on a network, as well as connecting.
#server.py will ask for the port to be listening on. Please input the port that you would like this server to listen onto.
#Ref: 
#https://realpython.com/python-sockets/
#chatGPT (debugging)


def listenForMessage(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Received from client: {data}")
        response = f"Server received: {data}"
        client_socket.send("Message received.".encode('utf-8'))
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   #This is where you will select what port you would like the server.py on this pc to listen on.
    port_str = input("Enter the port you would like to lsiten on: ")
    port = int(port_str)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print("[*] Listening on 0.0.0.0:" + port_str)

    while True:
        client, addr = server.accept()
        print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")
        messageListnening = threading.Thread(target=listenForMessage, args=(client,))
        messageListnening.start()

if __name__ == "__main__":
    start_server()
