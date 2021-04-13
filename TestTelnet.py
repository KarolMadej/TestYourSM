import telnetlib, re


def connect(host, user, passwd):
    countLOG = 0
    countPAS = 0
    s = telnetlib.Telnet(host)
    #Login
    with open("Bazy/BazaTelnetLogin.txt", 'r') as BazaLog:
        output = s.read_until(str.encode(": "), 2)
        for line in BazaLog:
            login = line.strip('\r\n')
            if re.search(login, bytes.decode(output)):
                try:
                    countLOG += 1
                    s.write(user.encode() + b"\n")
                    break
                except:
                    return 2

    #Password
    with open("Bazy/BazaTelnetPass.txt", 'r') as BazaPas:
        output = s.read_until(str.encode(": "), 2)
        for line in BazaPas:
            passd = line.strip('\r\n')
            if re.search(passd, bytes.decode(output)):
                try:
                    countPAS += 1
                    s.write(passwd.encode() + b"\n")
                    break
                except:
                    return 2

    try:
        (i,obj,byt) = s.expect([b'inncorect',b'@'],2)
    except:
        return 2
    if countLOG == 0 or countPAS == 0:
        return 2
    if i == 1:
        return 0
    s.close()
    return 1


def Main(host):
    result = 1
    with open("Bazy/BazaID1.txt", 'r') as a, open("Bazy/BazaHa1.txt", 'r') as b:
            for line1 in a:
                if result == 1:
                    user = line1.strip('\r\n')
                    b.seek(0)
                for line in b:
                    if result == 1:
                        passwd = line.strip('\r\n')
                        result = connect(host, user, passwd)


            if result == 0:
                return "Your password is weak"
            elif result == 1:
                return "Telnet connection is safe"
            elif result == 2:
                return "Error/Unknown server response"
