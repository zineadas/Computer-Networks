import socket

def client_program():
    host=socket.gethostname()
    port=5001

    client_socket=socket.socket()
    client_socket.connect((host,port))

    print(client_socket.recv(1024).decode())
    message=input("Enter date in format DD/MM/YYYY- > ")

    while message.lower().strip()!="bye":
        client_socket.send(message.encode())
        data=client_socket.recv(1024).decode()
        if str(data)=='0':
            print("Invalid Date")
        else:
            print("Valid Date")

        message=input("Enter date in format DD/MM/YYYY -> ")

    client_socket.close()


if __name__=="__main__":
    client_program()