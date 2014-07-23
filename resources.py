from myimport import *

DATETIME_FORMAT = "yyyy-MM"

def globaldb():
    db = QSqlDatabase.addDatabase("QMYSQL")
    db.setHostName("")
    db.setHostName("218.16.248.155")
    db.setDatabaseName("kfother")
    db.setUserName("kfk")
    db.setPassword("kfk123456")
    # db.setDatabaseName("caracate.db")
    if not db.open():
        QMessageBox.warning(None, "Phone Log",  "Database Error: %s" % db.lastError().text())
        sys.exit(1)
    return db