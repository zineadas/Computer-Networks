import socket

def countVowels(s):
    c=0
    for ch in s:
        if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
            c+=1
    return c

def server_program():
    print("Server Started!")
    host=''
    port=5000

    server_socket=socket.socket()
    server_socket.bind((host,port))

    server_socket.listen(5)
    conn,addr=server_socket.accept()
    print("Connected to "+"Host "+str(addr[0])+ "| Port "+str(addr[1]))
    conn.send("Welcome to Server Z".encode())

    while True:
        data=conn.recv(1024).decode()
        if not data:
            print("Connection closed. ")
            break
        print("Received data: "+str(data))
        n=countVowels(str(data).lower())
        conn.send(str(n).encode())

    conn.close()

if __name__=="__main__":
    server_program()

