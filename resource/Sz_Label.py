from PyQt5.Qt import *


class SzLabel(QLabel):

    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        print(evt.pos())

        point = QPushButton(self)
        point.resize(20, 20)
        point.move(evt.pos()-QPoint(10, 10))
        point.setStyleSheet("background-color: yellow; border-radius: 10px;")
        point.show()

        point.clicked.connect(lambda _, btn=point: btn.deleteLater())