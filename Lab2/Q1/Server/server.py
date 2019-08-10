import socket
import os

def sendFile(fname,obj):
    print('File sent')
    os.system("cp " + fname + " ../Proxy")
    obj.send("File sent".encode())

def server_program():
    host=socket.gethostname()
    port=5000

    server_socket=socket.socket()
    server_socket.bind((host,port))

    server_socket.listen(5)
    conn,address=server_socket.accept()
    print("Connection from proxy server: "+str(address))

    data=conn.recv(1024).decode()
    while True:
        if data:
            print("From proxy server: "+str(data))

            fname=str(data)
            if os.path.isfile(fname):
                sendFile(fname,conn)
            else:
                print("File does not exist")
                conn.send("nil".encode())
        data=conn.recv(1024).decode()

    conn.close()


if __name__=='__main__':
    server_program()