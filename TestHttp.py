import time as t
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def Main(website):
    b = open("Bazy/BazaHa1.txt", 'r')
    a = open("Bazy/BazaID1.txt", 'r')
    x = open("Http/PSEL.txt", 'r')
    y = open("Http/USEL.txt", 'r')
    z = open("Http/BSEL.txt", 'r')
    optionss = webdriver.ChromeOptions()
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    browser = webdriver.Chrome(chrome_options=optionss)
    browser.get(website)
    new_website = browser.current_url
    try:
        for line1 in a:
                user = line1.strip('\r\n')
                b.seek(0)
                for line in b:
                    passwd = line.strip('\r\n')
                    t.sleep(2)
                    new_website = browser.current_url
                    if new_website == website:
                        browser.get(website)
                        t.sleep(2)

                        y.seek(0)
                        for line in y:
                            try:
                                Sel_user = browser.find_element_by_css_selector(line)
                                break
                            except:
                                if line == "END":
                                    browser.__exit__()
                                    return "Unknown user selector"
                                continue
                        x.seek(0)
                        for line in x:
                            try:
                                    Sel_pas = browser.find_element_by_css_selector(line)
                                    break
                            except:
                                if line == "END":
                                    browser.__exit__()
                                    return "Unknown password selector"
                                continue
                        z.seek(0)
                        for line in z:
                            try:
                                enter = browser.find_element_by_css_selector(line)
                                break
                            except:
                                if line == "END":
                                    browser.__exit__()
                                    return "Unknown button selector"
                                continue

                        Sel_user.send_keys(user)
                        Sel_pas.send_keys(passwd)
                        enter.send_keys(Keys.ENTER)
                        t.sleep(5)
                    else:
                        browser.__exit__()
                        return "Weak password"
        browser.__exit__()
        return "Strong password"
    except:
        return "Unknown ERROR"