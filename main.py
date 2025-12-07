from app.gui.main_window import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

app = QApplication([])
app.setWindowIcon(QIcon("icon.png"))
window = MainWindow()
window.show()
app.exec()