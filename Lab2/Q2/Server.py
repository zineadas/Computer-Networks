import socket
from numpy import inf

def getRecord_HighestSalary(emp):
    max_sal=-inf
    for sublist in emp:
        if int(sublist[1])>max_sal:
            max_sal=int(sublist[1])
    s=""
    for sublist in emp:
        if int(sublist[1])==max_sal:
            s=s+" ".join(sublist)+"\n"
    return s

def getRecord_DeptName(d,emp):
    s=""
    for i,sublist in enumerate(emp):
        if sublist[-1]==d:
            s=s+" ".join(sublist)+"\n"
    return s

def getRecord_HighestEmpCount(emp,dept):
    max_count=-inf
    for sublist in dept:
        if int(sublist[1])>max_count:
            max_count=int(sublist[1])
            d=sublist[0]
    s=""
    for sublist in emp:
        if sublist[-1]==d:
            s=s+" ".join(sublist)+"\n"
    return s

def getRecord_SecondHighestSalary(emp):
    first_max=max(int(emp[0][1]),int(emp[1][1]))
    second_max=min(int(emp[0][1]),int(emp[1][1]))
    for i in range(2,len(emp)):
        if int(emp[i][1])>first_max:
            second_max=first_max
            first_max=int(emp[i][1])
        else:
            if int(emp[i][1])>second_max:
                second_max=int(emp[i][1])
    s=""
    for sublist in emp:
        if int(sublist[1])==second_max:
            s=s+" ".join(sublist)+"\n"
    return s

def switchCase(x,dept,emp):
    x=x.split(" ")
    if x[0]=='0':
        result=getRecord_HighestSalary(emp)
    elif x[0]=='1':
        d=x[1]
        result=getRecord_DeptName(d,emp)
    elif x[0]=='2':
        result=getRecord_HighestEmpCount(emp,dept)
    elif x[0]=='3':
        result=getRecord_SecondHighestSalary(emp)
    print(result)
    return result

def readFiles():
    f = open('Department.txt', "r")
    lines = f.readlines()[1:]
    department = []
    for x in lines:
        str = " ".join(x.split())
        department.append(list(str.split(" ")))
    f.close()

    f = open('Employee.txt', "r")
    lines = f.readlines()[1:]
    employee = []
    for x in lines:
        str = " ".join(x.split())
        employee.append(list(str.split(" ")))
    f.close()

    return (department,employee)

def server_program(dept,emp):
    host=socket.gethostname()
    port=5001
    server_socket=socket.socket()
    server_socket.bind((host,port))
    server_socket.listen(2)
    conn,address=server_socket.accept()
    print("Connection from: "+str(address))
    while True:
        data=conn.recv(1024).decode()
        if data:
            print("From connected client: "+str(data))

            y = switchCase(data,dept,emp)
            conn.send(y.encode())
    conn.close()

if __name__=='__main__':
    dept,emp=readFiles()
    server_program(dept,emp)