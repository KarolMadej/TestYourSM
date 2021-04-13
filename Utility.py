import socket

def Scan(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host,port))
        return True
    except:
        return False


def CheckIPFormat(IP):
    try:
        socket.inet_aton(IP)
        return True
    except socket.error:
        return  False

