import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog,QLineEdit
import UI
import requests
import TestSSH
import Utility
import TestTelnet
import TestHttp
import TestFTP

global IP
IP = ""


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = UI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonOK.clicked.connect(self.OKbutton)
        self.ui.pushButtonSSH.clicked.connect(self.SSHbutton)
        self.ui.pushButtonTelnet.clicked.connect(self.Telnetbutton)
        self.ui.pushButtonHTTP.clicked.connect(self.HTTPbutton)
        self.ui.pushButtonFTP.clicked.connect(self.FTPbutton)
        self.show()

    def OKbutton(self):
        global IP
        IP = self.ui.IPLine.text()
        if Utility.CheckIPFormat(IP):
            self.ui.label_2.setText("Your device IP: " + str(IP))
        else:
            self.ui.label_2.setText("Wrong IP format")

    def SSHbutton(self):
        if IP == "":
            self.ui.label_4.setText("Please check your IP")
        else:
             if(Utility.Scan(IP,22)) == True:
                TestSSH.Main(IP)
                if TestSSH.Error != "":
                    self.ui.label_4.setText("Connection error")
                else:
                     if(TestSSH.FoundID != "" and TestSSH.FoundPass != ""):
                         self.ui.label_4.setText("Your password is weak")
                     else:
                         self.ui.label_4.setText("SSH connection is safe")
             else:
                 self.ui.label_4.setText("Port 22 is closed")


    def Telnetbutton(self):
        if IP == "":
            self.ui.label_5.setText("Please check your IP")
        else:
             if(Utility.Scan(IP,23)) == True:
                 result = TestTelnet.Main(IP)
                 self.ui.label_5.setText(result)
             else:
                 self.ui.label_5.setText("Port 23 is closed")


    def FTPbutton(self):
        if IP == "":
            self.ui.label_9.setText("Please check your IP")
        else:
            if (Utility.Scan(IP, 21)) == True:
                TestFTP.Main(IP)
                if (TestFTP.FoundIDF != "" and TestFTP.FoundPassF != ""):
                    self.ui.label_9.setText("Your password is weak")
                else:
                    self.ui.label_9.setText("FTP connection is safe")
            else:
                self.ui.label_9.setText("Port 21 is closed")



    def HTTPbutton(self):
        website = ""
        website = self.ui.WebLine.text()
        if website != "":
            request = requests.get(website)
            if request.status_code == 200:
                result = TestHttp.Main(website)
                self.ui.label_8.setText(result)
            else:
                self.ui.label_8.setText("Wrong URL")
        else:
            self.ui.label_8.setText("Please write URL address")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
