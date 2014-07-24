# from PyQt4 import 
from myimport import *
from resources import *
from frmMain import MainWindow

class Login(QDialog):
    def __init__(self, db=""):
        QDialog.__init__(self)

        if db == "":
            self.db = globaldb()
        else:
            self.db = db

        lbl1 = QLabel("用户名：")
        lbl2 = QLabel("密  码：")

        self.textName = QLineEdit()
        self.textPass = QLineEdit()
        self.buttonLogin = QPushButton('登录')

        self.textName.setFixedWidth(100)
        self.textPass.setFixedWidth(100)
        self.buttonLogin.setFixedWidth(100)
        self.buttonLogin.clicked.connect(self.handleLogin)

        layout = QGridLayout()
        layout.addWidget(lbl1, 0, 0, Qt.AlignRight)
        layout.addWidget(self.textName, 0, 1)
        layout.addWidget(lbl2, 1, 0, Qt.AlignRight)
        layout.addWidget(self.textPass, 1, 1)
        layout.addWidget(self.buttonLogin, 2, 1)

        bitmaplbl = QLabel()
        bitmaplbl.setPixmap(QPixmap("images/login.png"))
        hlayout = QHBoxLayout()
        hlayout.addWidget(bitmaplbl)
        hlayout.addLayout(layout)

        self.setLayout(hlayout)

        self.setWindowTitle("汕头市残联康复业务系统")
        self.setWindowIcon(QIcon("images/login.png"))
        self.setStyleSheet("font-size:16px;")

        self.setMinimumSize(320,180)
        self.setMaximumSize (320,180)
        self.resize(320,180)

    def handleLogin(self):
        username = self.textName.text()
        passwd   = self.textPass.text()

        query = QSqlQuery(self.db)
        strsql = "SELECT unitsn, unitname, unitclass,unitman FROM User where unitsn='%s' and passwd='%s'" % (username, passwd)
        ret= query.exec_(strsql);
        # print(ret, "~~~~~~~", strsql, query.next(), query.isValid())
        # print(ret, query.isValid(), query.next(),)
        if query.next():
            curuser = {}
            curuser['unitsn']      = query.value(0)
            curuser['unitname']    = query.value(1)
            curuser['unitclass']   = query.value(2)
            curuser['unitman']     = query.value(3)
            # print("user", curuser)
            self.accept()
        else:
            QMessageBox.warning(self, '错误', '请输入正确的用户名和密码')

def DispLogin():
    import sys
    app = QApplication(sys.argv)

    db = globaldb()
    loginwin = Login(db)
    if loginwin.exec_() == QDialog.Accepted:
        window = MainWindow(db)
        window.show()
        sys.exit(app.exec_())

                
if __name__ == '__main__':
    DispLogin()