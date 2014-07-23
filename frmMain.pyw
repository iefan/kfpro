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
        self.createDb()

        widget = UserDlg(db=self.db)
        widget2 = AdaptDlg(db=self.db)
        self.tabWidget.addTab(widget,"用户管理")
        self.tabWidget.addTab(widget2,"适配器管理")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.closeMyTab)

        self.infoLabel = widget.infoLabel
        
        self.setCentralWidget(self.tabWidget)


        self.createActions()
        self.createMenus()

        message = "A context menu is available by right-clicking"
        self.statusBar().showMessage(message)

        self.setWindowTitle("康复业务系统")
        self.setMinimumSize(480,320)
        self.resize(720,600)

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
            isover bool default false);"
        # strsql = "create table MyClass(id int(4) not null primary key auto_increment, name char(20) not null, sex int(4) not null default '0', degree double(16,2));"

        ret = query.exec_(strsqlAdapt)
        # print(ret)
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

    def newFile(self):
        self.infoLabel.setText("Invoked <b>File|New</b>")

    def open(self):
        self.infoLabel.setText("Invoked <b>File|Open</b>")
        	
    def save(self):
        self.infoLabel.setText("Invoked <b>File|Save</b>")

    def print_(self):
        self.infoLabel.setText("Invoked <b>File|Print</b>")

    def undo(self):
        self.infoLabel.setText("Invoked <b>Edit|Undo</b>")

    def redo(self):
        self.infoLabel.setText("Invoked <b>Edit|Redo</b>")

    def cut(self):
        self.infoLabel.setText("Invoked <b>Edit|Cut</b>")

    def copy(self):
        self.infoLabel.setText("Invoked <b>Edit|Copy</b>")

    def paste(self):
        self.infoLabel.setText("Invoked <b>Edit|Paste</b>")

    def bold(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Bold</b>")

    def italic(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Italic</b>")

    def leftAlign(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Left Align</b>")

    def rightAlign(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Right Align</b>")

    def justify(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Justify</b>")

    def center(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Center</b>")

    def setLineSpacing(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Set Line Spacing</b>")

    def setParagraphSpacing(self):
        self.infoLabel.setText("Invoked <b>Edit|Format|Set Paragraph Spacing</b>")

    def about(self):
        self.infoLabel.setText("Invoked <b>Help|About</b>")
        QMessageBox.about(self, "About Menu",
                "The <b>Menu</b> example shows how to create menu-bar menus "
                "and context menus.")

    def aboutQt(self):
        self.infoLabel.setText("Invoked <b>Help|About Qt</b>")


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
        self.newAct     = self.createAction("新建(&N)", self.newFile,   QKeySequence.New, "", "创建一个新的用户")
        self.openAct    = self.createAction("&Open...", self.open,   QKeySequence.Open, "", "Open an existing file")
        self.saveAct    = self.createAction("&Save", self.save,   QKeySequence.Save, "", "Save the document to disk")
        self.printAct   = self.createAction("&Print...", self.print_,   QKeySequence.Print, "", "Print the document")
        self.exitAct    = self.createAction("E&xit", self.close,   "Ctrl+Q", "", "Exit the application")
        self.undoAct    = self.createAction("&Undo", self.undo,   QKeySequence.Undo, "", "Undo the last operation")
        self.redoAct    = self.createAction("&Redo", self.redo,   QKeySequence.Redo, "", "Redo the last operation")
        self.cutAct     = self.createAction("Cu&t", self.cut,   QKeySequence.Cut, "", "Cut the current selection's contents to the clipboard")
        self.copyAct    = self.createAction("&Copy", self.copy,   QKeySequence.Copy, "", "Copy the current selection's contents to the clipboard")
        self.pasteAct   = self.createAction("&Paste", self.paste,   QKeySequence.Paste, "", "Paste the clipboard's contents")
        
        self.boldAct    = self.createAction("&Bold", self.bold,   "Ctrl+B", "", "Make the text bold", True)
        boldFont = self.boldAct.font()
        boldFont.setBold(True)
        self.boldAct.setFont(boldFont)

        self.italicAct  = self.createAction("&Italic", self.italic,   "Ctrl+I", "", "Make the text italic", True)
        italicFont = self.italicAct.font()
        italicFont.setItalic(True)
        self.italicAct.setFont(italicFont)

        self.setLineSpacingAct      = self.createAction("Set &Line Spacing...", self.setLineSpacing,   "", "", "Change the gap...")
        self.setParagraphSpacingAct = self.createAction("Set &Paragraph Spacing...", self.setParagraphSpacing,   "", "", "Change the gap between paragraphs")
        self.aboutAct   = self.createAction("&About", self.about,   "", "", "Show the application's About box")
        self.aboutQtAct = self.createAction("About &Qt", self.aboutQt,   "", "", "Show the Qt library's About box")
        self.aboutQtAct.triggered.connect(qApp.aboutQt)
  
        self.leftAlignAct  = self.createAction("&Left Align", self.leftAlign,  "Ctrl+L", "", "Left align the selected text", True)
        self.rightAlignAct = self.createAction("&Right Align", self.rightAlign,  "Ctrl+R", "", "Right align the selected text", True)
        self.justifyAct = self.createAction("&Justify", self.justify,  "Ctrl+J", "", "Justify the selected text", True)
        self.centerAct  = self.createAction("&Center", self.center,  "Ctrl+C", "", "Center the selected text", True)

        self.alignmentGroup = QActionGroup(self)
        self.alignmentGroup.addAction(self.leftAlignAct)
        self.alignmentGroup.addAction(self.rightAlignAct)
        self.alignmentGroup.addAction(self.justifyAct)
        self.alignmentGroup.addAction(self.centerAct)
        self.leftAlignAct.setChecked(True)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.printAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.editMenu = self.menuBar().addMenu("&Edit")
        self.editMenu.addAction(self.undoAct)
        self.editMenu.addAction(self.redoAct)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.cutAct)
        self.editMenu.addAction(self.copyAct)
        self.editMenu.addAction(self.pasteAct)
        self.editMenu.addSeparator()

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

        self.formatMenu = self.editMenu.addMenu("&Format")
        self.formatMenu.addAction(self.boldAct)
        self.formatMenu.addAction(self.italicAct)
        self.formatMenu.addSeparator().setText("Alignment")
        self.formatMenu.addAction(self.leftAlignAct)
        self.formatMenu.addAction(self.rightAlignAct)
        self.formatMenu.addAction(self.justifyAct)
        self.formatMenu.addAction(self.centerAct)
        self.formatMenu.addSeparator()
        self.formatMenu.addAction(self.setLineSpacingAct)
        self.formatMenu.addAction(self.setParagraphSpacingAct)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
