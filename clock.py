from PyQt5.Qt import *
from PyQt5.QtWidgets import *


class Clock(QLCDNumber):
    def __init__(self,digits=5,parent =None):
        super(Clock,self).__init__(digits,parent)
        self.setFrameShape(QFrame.NoFrame)
        self.timer = QTimer()
        self.setFixedWidth(130)
        self.timer.timeout.connect(self._update)
        self.timer.start(1000)
    def _update(self):
        time = QTime.currentTime().toString()
        self.display(time[0:5])


