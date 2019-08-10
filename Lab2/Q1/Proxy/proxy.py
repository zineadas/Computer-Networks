import socket
import os.path

def proxyClient(fname):
    host = socket.gethostname()
    port = 5000
    proxyServer_server_socket = socket.socket()
    print("proxy client created")
    proxyServer_server_socket.connect((host, port))
    print("Getting file "+fname+" from Server...")
    message=fname

    proxyServer_server_socket.send(message.encode())
    data = proxyServer_server_socket.recv(1024).decode()
    if str(data)!="nil":
        print("Received file from Server.")
        sendFile(message,proxyServer_server_socket)
        proxyServer_server_socket.close()
        return True
    else:
        print("File not found.")
        return False

def sendFile(fname,obj):
    print('File sent')
    os.system("cp " + fname + " ../Client")
    #obj.send("File sent***".encode())

def proxyServer():
    host_c=socket.gethostname()
    port_c=6000

    proxyServer_client_socket = socket.socket()
    proxyServer_client_socket.bind((host_c, port_c))

    proxyServer_client_socket.listen(5)
    conn, address = proxyServer_client_socket.accept()
    print("Connection from client: " + str(address))

    while True:
        data=conn.recv(1024).decode()
        if data:
            print("File requested by Client: "+str(data))
            fname=str(data)
            if os.path.isfile(fname):
                sendFile(fname,conn)
                conn.send("File sent".encode())
            else:
                if proxyClient(fname):
                    conn.send("File sent".encode())
                else:
                    conn.send("nil".encode())

    conn.close()

if __name__=='__main__':
    proxyServer()