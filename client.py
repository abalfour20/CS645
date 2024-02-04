import socket

#This code will be the clientMain code (meaning the code that will be front facing).
#Messages will be sent from the cleint code to a listening server.
#listenMessage in server.py will recieve this message and display it. 
#Ref: 
#https://realpython.com/python-sockets/
#chatGPT (debugging)


def clientMain():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Enter the IP address of the other computer (can find from running IP config and looking at the ipv4 address)
    server_ip = input("Enter the server IP: ")
    #Enter the port the other computer's server.py is listening on.
    server_port = int(input("Enter the server port: "))

    client.connect((server_ip, server_port))

    while True:
        message = input("Type a message to send (press Enter to send): ")
        if message.lower() == 'exit':
            break
        client.send(message.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

    client.close()

if __name__ == "__main__":
    clientMain()
