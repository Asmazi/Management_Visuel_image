import sys
import threading


from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from clock import Clock
import connexion
class GUI(QMainWindow):
    def __init__(self, ap):
        super().__init__()
        self.app = ap
        self.initialize()
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.set()
    def initialize(self):
        self.setStyleSheet("QMainWindow{background-image : url('background.jpg');}")
    def set(self):
        self.setLogo()
        v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.image)
        self.c = Clock()
        self.h_layout.addWidget(self.c)
        self.h_layout.setAlignment(QtCore.Qt.AlignTop)
        self.w = QWidget()
        self.w.setLayout(self.h_layout)
        self.w.setFixedHeight(100)
        v_layout.addWidget(self.w)
        v_layout.addStretch(1)
        self.libreFrame()
        self.doAnimation(2000)

        widg = QWidget()
        widg.setLayout(v_layout)
        self.setCentralWidget(widg)
                #t=threading.Timer(10*(i+2*j), self.ecrire,args=[i])
                #t.start()

    def libreFrame(self):
        self.frame2 = QFrame(self)
        self.frame2.setStyleSheet("QGraphicsView{background : 'transparent';}")
        self.frame2.resize(400,400)
        self.frame2.move(100,100)
        self.label = QLabel(self.frame2)
        self.label.setGeometry(QtCore.QRect(60, 80, 700, 100))
        self.label.setStyleSheet("font: 75 28pt \"Elephant\";\n"
                                 "color: rgb(30, 116, 240);")
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.frame2)
        self.label_2.setGeometry(QtCore.QRect(60, 190, 700, 480))
        self.label_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
                              "color: rgb(58, 58, 58);")
        self.label_2.setWordWrap(True)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.label.setWordWrap(True)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Hello")

    def setLogo(self):
        logo = QPixmap('logo.png')
        self.image = QLabel()
        self.image.setPixmap(logo)
        self.image.resize(400, 400)

    ###############################################################

    def ecrire(self, i):

        self.label.setText(connexion.connexion()[i][0])
        self.label_2.setText(connexion.connexion()[i][1])
    def nbr(self):
        i = 0
        for row in connexion.connexion():
            i += 1
        return i
    def doAnimation(self,i):
        self.anim = QPropertyAnimation(self.frame2, b"geometry")
        self.anim.setLoopCount(i)
        self.anim.setDuration(10000)
        self.anim.setKeyValueAt(0, QRect(0, 150, 800, 600))
        self.anim.setKeyValueAt(0.1, QRect(300, 150, 800, 600))
        self.anim.setKeyValueAt(0.9, QRect(300.1, 150, 800, 600))
        self.anim.setKeyValueAt(1, QRect(1400, 150, 800, 600))
        self.anim.start()

    def parcourir(self):
        for j in range (0,1000):
            for i in range(0, 5):
                self.ecrire(i)
                QTest.qWait(10000)

    def closeEvent(self, *args, **kwargs):
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI(app)
    gui.showFullScreen()
    while True:
        gui.parcourir()
