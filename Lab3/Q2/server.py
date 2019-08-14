import socket

def isLeap(year):
    if ((year%400==0) or (year%4==0 and year%100!=0)):
        return True
    return False

def checkValidity(date):
    day,month,year=date.split('/')
    month_31=[1,3,5,7,8,10,12]
    month_30=[4,6,9,11]
    if int(month)==2:
        if isLeap(int(year)):
            if int(day)<1 or int(day)>29:
                return 0
        else:
            if int(day)<1 or int(day)>28:
                return 0
    elif int(month) in month_30:
        if int(day)<1 or int(day)>30:
            return 0
    elif int(month) in month_31:
        if int(day)<1 or int(day)>31:
            return 0
    return 1

def server_program():
    print("Server Started!")
    host=''
    port=5001

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
        n=checkValidity(str(data))
        print("Sent data: "+str(n))
        conn.send(str(n).encode())

    conn.close()

if __name__=="__main__":
    server_program()

