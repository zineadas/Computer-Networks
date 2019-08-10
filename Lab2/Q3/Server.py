import socket

def computeSum(s):
    if not s.isdigit():
        return "Sorry, cannot compute!"

    Sum=0
    for ch in s:
        Sum=Sum+int(ch)
    return str(Sum)

def server_program():
    host=''
    port=5001
    server_socket=socket.socket()
    server_socket.bind((host,port))
    server_socket.listen(2)
    conn,adress=server_socket.accept()
    print("Connection from: "+str(adress))
    while True:
        data=conn.recv(1024).decode()
        if not data:
            break
        print("Received from client: "+str(data))
        conn.send(computeSum(data).encode())
    conn.close()

if __name__=="__main__":
    server_program()