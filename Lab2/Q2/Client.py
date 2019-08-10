import socket

def client_program():
    host=socket.gethostname()
    port=5001
    client_socket=socket.socket()
    client_socket.connect((host,port))
    print("0 Display the record of employee with highest salary.\n1 Display the record of employees(name, salary and department_name) with particular Department_Name (taken as input from terminal).\n2 Display the record of employees (name, salary and department_name) who belong to the department with highest Employee_Count.\n3 Display record of the employee (name, salary and department_name) with second highest salary.\n")
    message=input("Enter no. \n<0>\n or <1 Dept name>\n or <2>\n or 3 or <bye> to exit -> ")
    while message.lower().strip()!='bye':
        client_socket.send(message.encode())
        data=client_socket.recv(1024).decode()
        print('Received answer: '+data)
        message=input("Enter no.: ")

    client_socket.close()


if __name__=='__main__':
    client_program()