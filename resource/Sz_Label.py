from PyQt5.Qt import *


class SzLabel(QLabel):

    def auto_add_point(self, result):
        w = self.width() / 4
        h = (self.height() - 30) /2
        for idx_s in result:
            idx_i = int(idx_s)
            row = (idx_i - 1) // 4
            col = (idx_i -1) % 4

            center_x = col * w + 0.5 * col
            center_y = 30 + row*h + h*0.5

    def clear_points(self):
        [child.deleteLater() for child in self.children() if child.inherits("QPushButton")]

    def get_result(self):
        # 12,13,45,56
        result = ",".join(["{},{}".format(child.x()+10, child.y()-20) for child in self.children() if child.inherits("QPushButton")])
        return result
        # for child in self.children():
        #     if child.inherits("QPushButton"):
        #         print(child.pos())

    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.x() < 0 or evt.y() <= 30:
            return None
        self.create_point_btn(evt.pos() - QPoint(10, 10))

    def create_point_btn(self, pt):
        point = QPushButton(self)
        point.resize(20, 20)
        point.move(pt)
        point.setStyleSheet("background-color: yellow; border-radius: 10px;")
        point.show()

        point.clicked.connect(lambda _, btn=point: btn.deleteLater())