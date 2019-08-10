import socket
import os.path

def client_program():
    host=socket.gethostname()
    port=6000

    client_socket=socket.socket()
    client_socket.connect((host,port))

    message=input('Enter name of file -> ')

    while  message.lower().strip()!='bye':
        if os.path.isfile(message):
            print("You already have this file!")
        else:
            client_socket.send(message.encode())
            data=client_socket.recv(1024).decode()
            if str(data)!="nil":
                print('Received file. ')
            else:
                print('File not found.')

        message=input('Enter name of file ->')

    client_socket.close()

if __name__ == '__main__':
    client_program()