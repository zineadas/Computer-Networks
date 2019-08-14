import socket

def client_program():
    host=socket.gethostname()
    port=5000

    client_socket=socket.socket()
    client_socket.connect((host,port))

    print(client_socket.recv(1024).decode())
    message=input("Enter string - > ")

    while message.lower().strip()!="bye":
        client_socket.send(message.encode())
        data=client_socket.recv(1024).decode()
        print("No. of vowels: "+data)

        message=input("Enter string -> ")

    client_socket.close()


if __name__=="__main__":
    client_program()