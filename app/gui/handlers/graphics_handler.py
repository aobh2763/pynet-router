from PySide6.QtWidgets import QGraphicsScene, QGraphicsView
from PySide6.QtGui import QPen, QColor
from PySide6.QtCore import Qt

class GraphicsHandler:
    def __init__(self, view: QGraphicsView, grid_size=40):
        self.view = view
        self.grid_size = grid_size
        self.width = view.width()
        self.height = view.height()
        self.origin_x = self.width // 8
        self.origin_y = (self.height // 8) * 7

        self.normal_pen = QPen(QColor(0, 0, 0, 100))
        self.normal_pen.setWidth(1)
        self.bold_pen = QPen(QColor(0, 0, 0))
        self.bold_pen.setWidth(2)

        self.scene = QGraphicsScene(0, 0, self.width, self.height)
        self.scene.setBackgroundBrush(Qt.white)
        self.view.setScene(self.scene)

        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setDragMode(self.view.DragMode.NoDrag)

        self.draw_grid()

    def draw_grid(self):
        self.scene.clear()
        self.scene.setBackgroundBrush(Qt.white)

        # Vertical lines
        x = self.origin_x
        while x < self.width:
            pen = self.bold_pen if x == self.origin_x else self.normal_pen
            self.scene.addLine(x, 0, x, self.height, pen)
            x += self.grid_size
        x = self.origin_x - self.grid_size
        while x > 0:
            pen = self.normal_pen
            self.scene.addLine(x, 0, x, self.height, pen)
            x -= self.grid_size

        # Horizontal lines
        y = self.origin_y
        while y < self.height:
            pen = self.bold_pen if y == self.origin_y else self.normal_pen
            self.scene.addLine(0, y, self.width, y, pen)
            y += self.grid_size
        y = self.origin_y - self.grid_size
        while y > 0:
            pen = self.normal_pen
            self.scene.addLine(0, y, self.width, y, pen)
            y -= self.grid_size