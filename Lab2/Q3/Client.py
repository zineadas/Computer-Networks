import socket


def client_program():

    s=input('Enter in following format:\n <client ip 5001>\n')
    s=s.split(' ')
    host=s[1]
    port = int(s[2])
    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input("Enter string: ")  # take input

    while len(message)!=1 and message!='Sorry, cannot compute!':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = data  # again take input

    client_socket.close()  # close the connection

if __name__=='__main__':
    client_program()