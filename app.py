import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def portScan(target, port):
    try:
        con = sock.connect((target, port))
        sock.settimeout(2)
        return True
    except Exception:
        return False


def main():
    host = input("Host address: ")
    lowerBound = int(input("Starting Port: "))
    upperBound = int(input("Endding Port: "))
    for x in range(lowerBound, upperBound):
        if (portScan(host, x)):
            print("Port ", x, " : Listening")
        else:
            print("Port ", x, " Not Listening")


main()
