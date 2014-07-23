#!/usr/bin/env python

# from PyQt4 import QtCore, QtGui
from myimport import *
from resources import globaldb
# from PyQt4.QtGui import QKeySequence, QAction, QIcon, QMainWindow, QApplication, QWidget, QSizePolicy, QLabel, QFrame, QTabWidget
# from PyQt4.QtGui import QVBoxLayout, qApp, QActionGroup, QMessageBox, QStandardItemModel, QTableView, QTableWidgetItem, QDialogButtonBox
# from PyQt4.QtGui import QPushButton, QStandardItem, QMenu, QItemDelegate, QStyleOptionComboBox, QComboBox, QAbstractItemView
# from PyQt4.QtCore import SIGNAL, Qt, QVariant, QPyNullVariant
# from PyQt4.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel

from frmUser import UserDlg
from frmAdapt import AdaptDlg

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # print(1)

        self.tabWidget=QTabWidget(self)

        self.db = globaldb()
        # self.createDb()

        # widget = UserDlg(db=self.db)
        # widget2 = AdaptDlg(db=self.db)
        # self.tabWidget.addTab(widget,"用户管理")
        # self.tabWidget.addTab(widget2,"适配器管理")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.closeMyTab)

        # self.infoLabel = widget.infoLabel
        
        self.setCentralWidget(self.tabWidget)


        self.createActions()
        self.createMenus()

        message = "A context menu is available by right-clicking"
        self.statusBar().showMessage(message)

        self.setWindowTitle("康复业务系统")
        self.setMinimumSize(480,320)
        self.resize(720,600)
        # self.createDb()

    def closeMyTab(self, tabindx):
        self.tabWidget.removeTab (tabindx)
        # print(tabindx)

    def createDb(self):
        query = QSqlQuery(self.db)
        strsqlUser = "create table User (id int not null primary key auto_increment,\
            unitsn char(20) not null, \
            passwd char(20) not null, \
            unitname char(40) not null, \
            unitclass char(40) not null, \
            unitman  char(30) not null);"
        
        strsqlAdapt = "create table Adaptstat(id int not null primary key auto_increment,\
            adaptdate date not null, \
            adaptpersons int default 0, \
            adapttools int default 0, \
            isover char(10) default '否');"
        # strsql = "create table MyClass(id int(4) not null primary key auto_increment, name char(20) not null, sex int(4) not null default '0', degree double(16,2));"

        ret = query.exec_(strsqlAdapt)
        print(ret)
        # query.exec_("insert into user values(101, 'aa', 'bb', 'cc', 'dd', 'ee')")
        # query.exec_("select * from recipes")
        # while query.next():
        #     print(query.value(0), query.value(1), query.value(2))
            # starttime DATETIME NOT NULL,
        # print("createdb")

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction(self.cutAct)
        menu.addAction(self.copyAct)
        menu.addAction(self.pasteAct)
        menu.exec_(event.globalPos())

    def userManage(self):
        print("count:", self.tabWidget.count())
        tabindx = self.tabWidget.currentIndex()
        if tabindx != -1:
            print(self.tabWidget.tabText(tabindx))

        print(self.tabWidget.currentIndex())
        widget = UserDlg(db=self.db)
        self.tabWidget.addTab(widget,"用户管理")
        # self.infoLabel.setText("Invoked <b>File|New</b>")

    def ToolManage(self):
        widget2 = AdaptDlg(db=self.db)
        self.tabWidget.addTab(widget2,"适配器管理")
        # self.infoLabel.setText("Invoked <b>File|Open</b>")
        	
    def about(self):
        # self.infoLabel.setText("Invoked <b>Help|About</b>")
        QMessageBox.about(self, "About Menu",
                "The <b>Menu</b> example shows how to create menu-bar menus "
                "and context menus.")

    def aboutQt(self):
        pass
        # self.infoLabel.setText("Invoked <b>Help|About Qt</b>")


    def createAction(self, text, slot=None, shortcut=None, icon=None, tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action

    def createActions(self):
        self.userAct    = self.createAction("用户管理(&M)", self.userManage,   "", "", "用户管理")
        self.toolAct    = self.createAction("辅具用品(&M)", self.ToolManage,   "", "", "辅具用品数量统计")
        self.exitAct    = self.createAction("E&xit", self.close,   "Ctrl+Q", "", "Exit the application")
        self.aboutAct   = self.createAction("&About", self.about,   "", "", "Show the application's About box")
        self.aboutQtAct = self.createAction("About &Qt", self.aboutQt,   "", "", "Show the Qt library's About box")
        self.aboutQtAct.triggered.connect(qApp.aboutQt)
        
    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("系统管理")
        self.fileMenu.addAction(self.userAct)        
        self.fileMenu.addAction(self.exitAct)

        self.editMenu = self.menuBar().addMenu("业务管理")
        self.editMenu.addAction(self.toolAct)
        
        self.helpMenu = self.menuBar().addMenu("关于(&H)")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
