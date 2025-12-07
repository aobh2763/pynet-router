from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsTextItem
from PySide6.QtGui import QPen, QColor, QFont
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

        # === GRID LINES ===
        # Vertical lines
        x = self.origin_x
        while x < self.width:
            pen = self.bold_pen if x == self.origin_x else self.normal_pen
            self.scene.addLine(x, 0, x, self.height, pen)
            x += self.grid_size

        x = self.origin_x - self.grid_size
        while x > 0:
            self.scene.addLine(x, 0, x, self.height, self.normal_pen)
            x -= self.grid_size

        # Horizontal lines
        y = self.origin_y
        while y < self.height:
            pen = self.bold_pen if y == self.origin_y else self.normal_pen
            self.scene.addLine(0, y, self.width, y, pen)
            y += self.grid_size

        y = self.origin_y - self.grid_size
        while y > 0:
            self.scene.addLine(0, y, self.width, y, self.normal_pen)
            y -= self.grid_size

        # === LABEL FONT ===
        font = QFont()
        font.setBold(True)

        # === X-AXIS LABELS ===
        # Positive x
        num = 2
        x = self.origin_x + self.grid_size * 2
        while x < self.width:
            text = self.scene.addText(str(num), font)
            text.setDefaultTextColor(Qt.black)
            br = text.boundingRect()
            text.setPos(x - br.width()/2, self.origin_y + 4)
            x += self.grid_size * 2
            num += 2

        # Negative x
        num = -2
        x = self.origin_x - self.grid_size * 2
        while x > 0:
            text = self.scene.addText(str(num), font)
            text.setDefaultTextColor(Qt.black)
            br = text.boundingRect()
            text.setPos(x - br.width()/2, self.origin_y + 4)
            x -= self.grid_size * 2
            num -= 2

        # === Y-AXIS LABELS ===
        # Negative direction first (down)
        num = -2
        y = self.origin_y + self.grid_size * 2
        while y < self.height:
            text = self.scene.addText(str(num), font)
            text.setDefaultTextColor(Qt.black)
            br = text.boundingRect()
            text.setPos(self.origin_x - 8 - br.width(), y - br.height()/2)  # left of axis
            y += self.grid_size * 2
            num -= 2

        # Positive direction second (up)
        num = 2
        y = self.origin_y - self.grid_size * 2
        while y > 0:
            text = self.scene.addText(str(num), font)
            text.setDefaultTextColor(Qt.black)
            br = text.boundingRect()
            text.setPos(self.origin_x - 8 - br.width(), y - br.height()/2)
            y -= self.grid_size * 2
            num += 2
    
    def draw_router(self, router):
        radius = 20
        x = self.origin_x + router.x * self.grid_size
        y = self.origin_y - router.y * self.grid_size
        
        move_down = 4

        # Thicker outline
        border_pen = QPen(Qt.black)
        border_pen.setWidth(3)

        # Professional-looking fill color (calm blue-gray)
        brush = QColor(135, 170, 220)

        # Draw router circle
        self.scene.addEllipse(
            x - radius, y - radius,
            radius * 2, radius * 2,
            border_pen,
            brush
        )

        # Router name above (slightly bigger, bold)
        name_item = QGraphicsTextItem(router.name)
        name_font = QFont()
        name_font.setBold(True)
        name_font.setPointSize(12)  # slightly bigger
        name_item.setFont(name_font)
        name_item.setDefaultTextColor(Qt.black)
        name_item.setPos(
            x - name_item.boundingRect().width() / 2,
            y - radius - 26
        )
        self.scene.addItem(name_item)

        # Router ID inside the circle (bold, white, slightly lower)
        id_item = QGraphicsTextItem(str(router.id))
        id_font = QFont()
        id_font.setBold(True)
        id_item.setFont(id_font)
        id_item.setDefaultTextColor(Qt.white)
        id_item.setPos(
            x - id_item.boundingRect().width() / 2,
            y - id_item.boundingRect().height() / 2 + 4 + move_down
        )
        self.scene.addItem(id_item)

        # Firewall status letter F at top-right (green if enabled, red if disabled)
        f_item = QGraphicsTextItem("F")
        f_font = QFont()
        f_font.setBold(True)
        f_item.setFont(f_font)
        f_item.setDefaultTextColor(Qt.green if router.firewall_enabled else Qt.red)
        f_item.setPos(
            x + radius - f_item.boundingRect().width(),
            y - radius + move_down
        )
        self.scene.addItem(f_item)

        # Security level number at top-left (bold black)
        sec_item = QGraphicsTextItem(str(router.security_level))
        sec_font = QFont()
        sec_font.setBold(True)
        sec_item.setFont(sec_font)
        sec_item.setDefaultTextColor(Qt.black)
        sec_item.setPos(
            x - radius,
            y - radius + move_down
        )
        self.scene.addItem(sec_item)

    def draw_routers(self, network):
        for router in network.routers:
            self.draw_router(router)
            
    def draw_link(self, link):
        x1 = self.origin_x + link.routerA.x * self.grid_size
        y1 = self.origin_y - link.routerA.y * self.grid_size
        x2 = self.origin_x + link.routerB.x * self.grid_size
        y2 = self.origin_y - link.routerB.y * self.grid_size

        # Line
        pen = QPen(Qt.darkGray)
        pen.setWidth(3)
        self.scene.addLine(x1, y1, x2, y2, pen)

        # Midpoint
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2

        # Cost text (bold, black)
        cost_item = QGraphicsTextItem(str(link.cost))
        font = QFont()
        font.setBold(True)
        cost_item.setFont(font)
        cost_item.setDefaultTextColor(Qt.black)

        # Slightly above the line
        cost_item.setPos(mx - cost_item.boundingRect().width()/2,
                        my - cost_item.boundingRect().height() - 4)

        self.scene.addItem(cost_item)
        
    def draw_links(self, network):
        for router in network.routers:
            for link in router.links:
                if link.routerA == router:
                    self.draw_link(link)
    
    def update_graphics(self, network):
        self.draw_grid()
        
        self.draw_links(network)
        self.draw_routers(network)